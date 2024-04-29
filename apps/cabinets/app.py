from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CabinetsAppConfig(AppConfig):
    """Default configuration for Cabinets app."""

    name = "apps.cabinets"
    verbose_name = _("cabinets")

    def ready(self):
        # pylint: disable=unused-import
        import apps.cabinets.api.schemas  # noqa
