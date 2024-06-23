from django.db.utils import DataError
from django.test import TestCase

import factory

from apps.cabinets.models import Cabinet


class TestCabinetModel(TestCase):
    """Test cabinet model."""

    def test_valid_name_max_length(self) -> None:
        """Test valid name by max length."""
        with self.assertRaises(DataError):
            Cabinet.objects.create(
                number="a" * 61,
                description=factory.Faker("text"),
            )
