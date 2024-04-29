from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DoctorsAppConfig(AppConfig):
    """Default configuration for Doctors app."""

    name = "apps.doctors"
    verbose_name = _("Doctors")

    def ready(self):
        # pylint: disable=unused-import
        import apps.doctors.api.schemas  # noqa
