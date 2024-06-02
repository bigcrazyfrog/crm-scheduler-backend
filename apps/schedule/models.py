import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Schedule(BaseModel):
    """Default model for Schedule."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=60,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Schedule")
        verbose_name_plural = _("Schedule")

    def __repr__(self) -> str:
        return f"Schedule<{self.name}>"

    def __str__(self) -> str:
        return f"{self.name}"
