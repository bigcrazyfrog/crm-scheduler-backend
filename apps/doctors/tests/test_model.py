from django.db.utils import DataError
from django.test import TestCase

from apps.doctors.models import Doctor


class TestDoctorModel(TestCase):
    """Test doctor model."""

    def test_valid_name_max_length(self) -> None:
        """Test valid name by max length."""
        with self.assertRaises(DataError):
            Doctor.objects.create(
                first_name="a" * 31,
                last_name="a" * 31,
                father_name="a" * 31,
            )
