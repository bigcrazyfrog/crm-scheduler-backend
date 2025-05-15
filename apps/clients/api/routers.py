from ninja import NinjaAPI, Router

import apps.clients.api.handlers as client_handlers
from apps.core.api.schemas import Message
from apps.clients.api.schemas import ClientOut


def get_clients_router() -> Router:
    """Get clients router."""
    router = Router(tags=["clients"])

    router.add_api_operation(
        "/",
        ["GET"],
        client_handlers.all,
        response={200: list[ClientOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        client_handlers.add,
        response={201: ClientOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{client_id}",
        ["GET"],
        client_handlers.get,
        response={200: ClientOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{client_id}",
        ["PUT"],
        client_handlers.update,
        response={200: ClientOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{client_id}",
        ["DELETE"],
        client_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_clients_router(api: NinjaAPI) -> NinjaAPI:
    """Add clients router to REST API."""
    api.add_router("clients/", get_clients_router())
    return api
