"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):

    """Test the calc module."""

    def test_add_numbers(self):  # make sure it is named with prefix test_
        """Test adding numbers together."""

        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):  # make sure it is named with prefix test_
        """Test subtracting numbers."""

        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
