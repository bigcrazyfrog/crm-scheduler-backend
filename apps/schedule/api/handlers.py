from django.http import HttpRequest

from apps.schedule.api.schemas import ScheduleAdd, ScheduleOut
from apps.schedule.models import Schedule
from apps.core.api.schemas import Message


def all(
    request: HttpRequest,
) -> tuple[int, Message | ScheduleOut]:
    """Get a list of all existing schedule."""
    schedules = Schedule.objects.all()
    return 200, list(schedules)


def add(
    request: HttpRequest,
    schedule_data: ScheduleAdd,
) -> tuple[int, Message | list[ScheduleOut]]:
    """Add new Schedule to database."""
    schedule = Schedule.objects.create(
        name=schedule_data.name,
        description=schedule_data.description,
    )
    return 201, schedule


def get(
    request: HttpRequest,
    schedule_id: str,
) -> tuple[int, Message | ScheduleOut]:
    """Get existing schedule."""
    schedule = Schedule.objects.filter(
        id=schedule_id,
    ).first()
    if schedule is None:
        return 404, {"message": "Schedule not found"}

    return 200, schedule


def update(
    request: HttpRequest,
    schedule_id: str,
    schedule_data: ScheduleAdd,
) -> tuple[int, Message | ScheduleOut]:
    """Update existing schedule fields."""
    schedule = Schedule.objects.filter(
        id=schedule_id,
    ).first()
    if schedule is None:
        return 404, {"message": "Schedule not found"}

    schedule.name = schedule_data.name
    schedule.description = schedule_data.description
    schedule.save()

    return 200, schedule


def delete(
    request: HttpRequest,
    schedule_id: str,
) -> tuple[int, Message | ScheduleOut]:
    """Delete schedule from database."""
    schedule = Schedule.objects.filter(
        id=schedule_id,
    ).first()
    if schedule is None:
        return 404, {"message": "Schedule not found"}

    schedule.delete()
    return 200, {"message": "Successful delete"}
