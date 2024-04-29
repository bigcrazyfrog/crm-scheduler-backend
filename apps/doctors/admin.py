from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(BaseAdmin):
    """UI for `Doctor` model."""

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
            _("Cabinets"),
            {
                "fields": (
                    "priority_cabinet",
                    "cabinets",
                ),
            },
        ),
    )
