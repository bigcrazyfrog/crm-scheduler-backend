from django.http import HttpRequest

from apps.cabinets.models import Cabinet
from apps.core.api.schemas import Message
from apps.doctors.models import Doctor
from apps.intervals.api.schemas import IntervalAdd, IntervalOut
from apps.schedule.models import Schedule

from ..models import Interval


def all(
    request: HttpRequest,
) -> tuple[int, Message | IntervalOut]:
    """Get a list of all existing intervals."""
    intervals = Interval.objects.filter()
    return 200, list(intervals)


def add(
    request: HttpRequest,
    interval_data: IntervalAdd,
) -> tuple[int, Message | list[IntervalOut]]:
    """Add new interval to database."""
    doctor = Doctor.objects.filter(id=interval_data.doctor).first()
    if doctor is None:
        return 404, {"message": "Doctor not found"}

    schedule = Schedule.objects.filter(id=interval_data.schedule).first()
    if schedule is None:
        return 404, {"message": "Schedule not found"}

    cabinet = Cabinet.objects.filter(id=interval_data.cabinet).first()
    if cabinet is None and interval_data.cabinet is not None:
        return 404, {"message": "Cabinet not found"}

    interval = Interval.objects.create(
        start=interval_data.start,
        end=interval_data.end,
        cabinet=cabinet,
        doctor=doctor,
        schedule=schedule,
    )
    return 201, interval


def get(
    request: HttpRequest,
    interval_id: str,
) -> tuple[int, Message | IntervalOut]:
    """Get existing interval."""
    interval = Interval.objects.filter(
        id=interval_id,
    ).first()
    if interval is None:
        return 404, {"message": "Interval not found"}

    return 200, interval


def update(
    request: HttpRequest,
    interval_id: str,
    interval_data: IntervalAdd,
) -> tuple[int, Message | IntervalOut]:
    """Update existing interval fields."""
    interval = Interval.objects.filter(
        id=interval_id,
    ).first()
    if interval is None:
        return 404, {"message": "Interval not found"}

    doctor = Doctor.objects.filter(id=interval_data.doctor).first()
    if doctor is None:
        return 404, {"message": "Doctor not found"}

    schedule = Schedule.objects.filter(id=interval_data.schedule).first()
    if schedule is None:
        return 404, {"message": "Schedule not found"}

    cabinet = Cabinet.objects.filter(id=interval_data.cabinet).first()
    if cabinet is None and interval_data.cabinet is not None:
        return 404, {"message": "Cabinet not found"}

    interval.start = interval_data.start
    interval.end = interval_data.end
    interval.cabinet = cabinet
    interval.doctor = doctor
    interval.schedule = schedule
    interval.save()

    return 200, interval


def delete(
    request: HttpRequest,
    interval_id: str,
) -> tuple[int, Message | IntervalOut]:
    """Delete interval from database."""
    interval = Interval.objects.filter(
        id=interval_id,
    ).first()
    if interval is None:
        return 404, {"message": "Interval not found"}

    interval.delete()
    return 200, {"message": "Successful delete"}
