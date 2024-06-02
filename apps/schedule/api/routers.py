from ninja import NinjaAPI, Router

import apps.schedule.api.handlers as schedule_handlers
from apps.schedule.api.schemas import ScheduleOut
from apps.core.api.schemas import Message


def get_schedules_router() -> Router:
    """Get schedules router."""
    router = Router(tags=["schedules"])

    router.add_api_operation(
        "/",
        ["GET"],
        schedule_handlers.all,
        response={200: list[ScheduleOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        schedule_handlers.add,
        response={201: ScheduleOut, 400: Message},
    )

    router.add_api_operation(
        "/{schedule_id}",
        ["GET"],
        schedule_handlers.get,
        response={200: ScheduleOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{schedule_id}",
        ["PUT"],
        schedule_handlers.update,
        response={200: ScheduleOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{schedule_id}",
        ["DELETE"],
        schedule_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_schedules_router(api: NinjaAPI) -> NinjaAPI:
    """Add schedules router to REST API."""
    api.add_router("schedules/", get_schedules_router())
    return api
