import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Interval(BaseModel):
    """Default model for interval."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    start = models.DateTimeField()
    end = models.DateTimeField()
    doctor = models.ForeignKey(
        to="doctors.Doctor",
        related_name="intervals",
        verbose_name=_("doctor"),
        on_delete=models.CASCADE,
    )
    cabinet = models.ForeignKey(
        to="cabinets.Cabinet",
        related_name="intervals",
        verbose_name=_("cabinet"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = _("Interval")
        verbose_name_plural = _("Intervals")

    def __repr__(self) -> str:
        return f"Interval<{self.start} {self.end}>"

    def __str__(self) -> str:
        return f"{self.start} {self.end}"
