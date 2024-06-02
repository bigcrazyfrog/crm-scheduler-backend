import factory

from . import models


class ScheduleFactory(factory.django.DjangoModelFactory):
    """Factory to generate test cabinet instance."""

    name = factory.Faker("name")
    description = factory.Faker("text")

    class Meta:
        model = models.Schedule
