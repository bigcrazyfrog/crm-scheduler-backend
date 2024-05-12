from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AlgorithmAppConfig(AppConfig):
    """Default configuration for Algorithm app."""

    name = "apps.algorithm"
    verbose_name = _("algorithm")

