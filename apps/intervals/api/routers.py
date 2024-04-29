from ninja import NinjaAPI, Router

import apps.intervals.api.handlers as interval_handlers
from apps.core.api.schemas import Message
from apps.intervals.api.schemas import IntervalOut


def get_intervals_router() -> Router:
    """Get intervals router."""
    router = Router(tags=["intervals"])

    router.add_api_operation(
        "/",
        ["GET"],
        interval_handlers.all,
        response={200: list[IntervalOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        interval_handlers.add,
        response={201: IntervalOut, 400: Message},
    )

    router.add_api_operation(
        "/{interval_id}",
        ["GET"],
        interval_handlers.get,
        response={200: IntervalOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{interval_id}",
        ["PUT"],
        interval_handlers.update,
        response={200: IntervalOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{interval_id}",
        ["DELETE"],
        interval_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_intervals_router(api: NinjaAPI) -> NinjaAPI:
    """Add intervals router to REST API."""
    api.add_router("intervals/", get_intervals_router())
    return api
