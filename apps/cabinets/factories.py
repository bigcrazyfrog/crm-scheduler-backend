import factory

from . import models


class CabinetFactory(factory.django.DjangoModelFactory):
    """Factory to generate test cabinet instance."""

    number = factory.Faker("number")
    description = factory.Faker("text")

    class Meta:
        model = models.Cabinet
