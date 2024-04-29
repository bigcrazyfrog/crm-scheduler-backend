from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Interval


@admin.register(Interval)
class IntervalAdmin(BaseAdmin):
    """UI for `Interval` model."""

    ordering = (
        "start",
    )
    list_display = (
        "start",
        "end",
        "doctor",
        "cabinet",
    )
    search_fields = (
        "doctor",
        "cabinet",
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
            _("Time"),
            {
                "fields": (
                    "start",
                    "end",
                ),
            },
        ),
        (
            _("Info"),
            {
                "fields": (
                    "doctor",
                    "cabinet",
                ),
            },
        ),
    )
