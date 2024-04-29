import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Doctor(BaseModel):
    """Default model for doctor."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(
        verbose_name=_("Firstname"),
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name=_("Lastname"),
        max_length=30,
    )
    father_name = models.CharField(
        verbose_name=_("Fathername"),
        max_length=30,
        blank=True,
    )
    priority_cabinet = models.ForeignKey(
        to="cabinets.Cabinet",
        related_name="priority_doctors",
        verbose_name=_("Priority cabinet"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )
    cabinets = models.ManyToManyField(
        to="cabinets.Cabinet",
        related_name="doctors",
        verbose_name=_("Cabinet"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")

    def __repr__(self) -> str:
        return f"Doctor<{self.first_name} {self.last_name}>"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
