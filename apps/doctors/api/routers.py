from ninja import NinjaAPI, Router

import apps.doctors.api.handlers as doctor_handlers
from apps.core.api.schemas import Message
from apps.doctors.api.schemas import DoctorOut


def get_doctors_router() -> Router:
    """Get doctors router."""
    router = Router(tags=["doctors"])

    router.add_api_operation(
        "/",
        ["GET"],
        doctor_handlers.all,
        response={200: list[DoctorOut], 400: Message},
    )

    router.add_api_operation(
        "/{student_id}",
        ["GET"],
        doctor_handlers.get,
        response={200: DoctorOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{student_id}",
        ["DELETE"],
        doctor_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_doctors_router(api: NinjaAPI) -> NinjaAPI:
    """Add doctors router to REST API."""
    api.add_router("doctors/", get_doctors_router())
    return api
