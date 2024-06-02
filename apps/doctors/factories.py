import factory

from . import models


class DoctorFactory(factory.django.DjangoModelFactory):
    """Factory to generate test Doctor instance."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    father_name = factory.Faker("first_name")

    class Meta:
        model = models.Doctor
