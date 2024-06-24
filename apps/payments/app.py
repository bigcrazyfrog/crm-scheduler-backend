from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentsAppConfig(AppConfig):
    """Default configuration for Payments app."""

    name = "apps.payments"
    verbose_name = _("payments")

    def ready(self):
        # pylint: disable=unused-import
        import apps.payments.api.schemas  # noqa
