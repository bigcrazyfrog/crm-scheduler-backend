from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AlgorithmAppConfig(AppConfig):
    """Default configuration for Algorithm app."""

    name = "apps.algorithm"
    verbose_name = _("algorithm")

    def ready(self):
        # pylint: disable=unused-import
        import apps.algorithm.api.schemas  # noqa
