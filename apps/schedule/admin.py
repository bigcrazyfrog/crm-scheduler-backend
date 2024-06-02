from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(BaseAdmin):
    """UI for `Schedule` model."""

    ordering = (
        "name",
    )
    list_display = (
        "name",
        "description",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "id",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                    "name",
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
