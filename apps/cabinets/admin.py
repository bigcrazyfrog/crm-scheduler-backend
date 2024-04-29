from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Cabinet


@admin.register(Cabinet)
class CabinetAdmin(BaseAdmin):
    """UI for `Cabinet` model."""

    ordering = (
        "number",
    )
    list_display = (
        "number",
        "description",
    )
    search_fields = (
        "number",
    )
    readonly_fields = (
        "id",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                    "number",
                ),
            },
        ),
        (
            _("Content"),
            {
                "fields": (
                    "description",
                ),
            },
        ),
    )
