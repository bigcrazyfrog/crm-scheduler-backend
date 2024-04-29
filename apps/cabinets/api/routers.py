from ninja import NinjaAPI, Router

import apps.cabinets.api.handlers as cabinet_handlers
from apps.cabinets.api.schemas import CabinetOut
from apps.core.api.schemas import Message


def get_cabinets_router() -> Router:
    """Get cabinets router."""
    router = Router(tags=["cabinets"])

    router.add_api_operation(
        "/",
        ["GET"],
        cabinet_handlers.all,
        response={200: list[CabinetOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        cabinet_handlers.add,
        response={201: CabinetOut, 400: Message},
    )

    router.add_api_operation(
        "/{cabinet_id}",
        ["GET"],
        cabinet_handlers.get,
        response={200: CabinetOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{cabinet_id}",
        ["PUT"],
        cabinet_handlers.update,
        response={200: CabinetOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{cabinet_id}",
        ["DELETE"],
        cabinet_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_cabinets_router(api: NinjaAPI) -> NinjaAPI:
    """Add cabinets router to REST API."""
    api.add_router("cabinets/", get_cabinets_router())
    return api
