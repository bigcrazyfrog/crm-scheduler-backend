from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SchedulesAppConfig(AppConfig):
    """Default configuration for Schedules app."""

    name = "apps.schedule"
    verbose_name = _("schedules")

    def ready(self):
        # pylint: disable=unused-import
        import apps.schedule.api.schemas  # noqa
