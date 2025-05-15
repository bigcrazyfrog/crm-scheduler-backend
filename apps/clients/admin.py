from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Client


@admin.register(Client)
class ClientAdmin(BaseAdmin):
    """UI for `Client` model."""

    ordering = (
        "last_name",
    )
    list_display = (
        "first_name",
        "last_name",
        "father_name",
    )
    search_fields = (
        "last_name",
        "first_name",
    )
    readonly_fields = (
        "id",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                ),
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "father_name",
                ),
            },
        ),
        (
            _("Email"),
            {
                "fields": (
                    "email",
                ),
            },
        ),
    )
