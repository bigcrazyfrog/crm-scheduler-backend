from ninja import NinjaAPI, Router

import apps.algorithm.api.handlers as algorithms_handlers
from apps.core.api.schemas import Message


def get_algorithms_router() -> Router:
    """Get algorithms router."""
    router = Router(tags=["algorithms"])

    router.add_api_operation(
        "/clear_cabinets",
        ["GET"],
        algorithms_handlers.clear_cabinets,
        response={200: Message, 400: Message},
    )

    router.add_api_operation(
        "/v1",
        ["GET"],
        algorithms_handlers.v1,
        response={200: Message, 400: Message},
    )

    router.add_api_operation(
        "/v2",
        ["GET"],
        algorithms_handlers.v2,
        response={200: Message, 400: Message},
    )


    return router


def add_algorithms_router(api: NinjaAPI) -> NinjaAPI:
    """Add algorithms router to REST API."""
    api.add_router("algorithms/", get_algorithms_router())
    return api
