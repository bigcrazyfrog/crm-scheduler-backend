from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ClientsAppConfig(AppConfig):
    """Default configuration for Clients app."""

    name = "apps.clients"
    verbose_name = _("Clients")

    def ready(self):
        # pylint: disable=unused-import
        import apps.clients.api.schemas  # noqa
