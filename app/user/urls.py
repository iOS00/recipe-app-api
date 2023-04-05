"""
URL mappings for the user API.
"""
from django.urls import path

from user import views


app_name = 'user'  # used for reverse mapping reverse('user:create') in test file

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]  # maps create/ URL to our view from views.py of user app
