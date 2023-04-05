"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):  # to validate data and save to a model (class)
    """Serializer for the user object."""

    class Meta:  # define model for the serializer to store our data
        model = get_user_model()
        fields = ['email', 'password', 'name']  # needs to be provided in request (managed by this API)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}  # extra metadata

    def create(self, validated_data):  # override the default serializer, called if above validation passed
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):  # instance that will be updated
        """Update and return user."""
        password = validated_data.pop('password', None)  # retrieve and remove password if provided
        user = super().update(instance, validated_data)  # overriding update method from base serializer

        if password:  # if password is provided by user
            user.set_password(password)  # will be encrypted with hash
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):  # a base serializer class, not ModelSerializer
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )  # input_type: password will make a special hidden mode for typing in

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user  # if validation above passed it sets a 'user' attribute
        return attrs
