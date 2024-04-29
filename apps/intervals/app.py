from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IntervalsAppConfig(AppConfig):
    """Default configuration for Intervals app."""

    name = "apps.intervals"
    verbose_name = _("Intervals")

    def ready(self):
        # pylint: disable=unused-import
        import apps.intervals.api.schemas  # noqa
