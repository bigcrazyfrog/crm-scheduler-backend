import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Client(BaseModel):
    """Default model for client."""

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
    email = models.EmailField(
        verbose_name=_("Email"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __repr__(self) -> str:
        return f"Client<{self.first_name} {self.last_name}>"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
