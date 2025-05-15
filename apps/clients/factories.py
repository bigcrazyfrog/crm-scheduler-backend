import factory

from . import models


class ClientFactory(factory.django.DjangoModelFactory):
    """Factory to generate test Client instance."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    father_name = factory.Faker("first_name")

    class Meta:
        model = models.Client
