from ninja import NinjaAPI, Router

import apps.payments.api.handlers as payment_handlers
from apps.core.api.schemas import DefaultResponse, Message


def get_payments_router() -> Router:
    """Get payments router."""
    router = Router(tags=["payments"])

    router.add_api_operation(
        "/check",
        ["GET"],
        payment_handlers.check_payment,
        response={200: DefaultResponse, 400: Message},
    )

    router.add_api_operation(
        "/pay_link",
        ["GET"],
        payment_handlers.get_pay_link,
        response={200: DefaultResponse, 400: Message},
    )

    return router


def add_payments_router(api: NinjaAPI) -> NinjaAPI:
    """Add payments router to REST API."""
    api.add_router("payments/", get_payments_router())
    return api
