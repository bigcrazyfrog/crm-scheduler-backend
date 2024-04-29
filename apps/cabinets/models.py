import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Cabinet(BaseModel):
    """Default model for cabinet."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    number = models.CharField(
        verbose_name=_("Title"),
        max_length=60,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Cabinet")
        verbose_name_plural = _("Cabinet")

    def __repr__(self) -> str:
        return f"Cabinet<{self.number}>"

    def __str__(self) -> str:
        return f"{self.number}"
