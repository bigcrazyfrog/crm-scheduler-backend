from django.http import HttpRequest

from apps.algorithm.services import make_schedule, make_schedule_v2
from apps.algorithm.test_data.service import (
    generate_random_data_for_cabinets,
    generate_random_data_for_doctors,
    generate_random_data_for_intervals,
    remove_all_data,
)
from apps.core.api.schemas import Message
from apps.doctors.models import Doctor
from apps.intervals.models import Interval


def clear_cabinets(request: HttpRequest) -> tuple[int, Message]:
    """Clear all cabinets."""
    intervals = Interval.objects.exclude(cabinet=None)
    number = intervals.count()
    intervals.update(cabinet=None)
    return 200, Message(message=f"{number} cabinets cleared!")


def v1(
    request: HttpRequest,
) -> tuple[int, Message]:
    """No coments... What is it???"""
    doctors = Doctor.objects.all().prefetch_related("cabinets")
    intervals = Interval.objects.all().select_related("cabinet", "doctor")

    make_schedule(doctors, intervals)
    return 200, {"message": "Success"}


def v2(request: HttpRequest) -> tuple[int, Message]:
    """v2 for alghoritms."""
    doctors = Doctor.objects.prefetch_related("cabinets")
    intervals = Interval.objects.all().select_related("cabinet", "doctor")

    make_schedule_v2(doctors, intervals)
    return 200, {"message": "Success"}


def generate_intervals(request: HttpRequest) -> tuple[int, Message]:
    """Generate intervals for alghoritms."""
    if generate_random_data_for_intervals():
        return 200, {"message": "Success"}
    return 400, {"message": "Errror"}


def generate_cabinets(request: HttpRequest) -> tuple[int, Message]:
    """Generate cabinets for alghoritms."""
    if generate_random_data_for_cabinets():
        return 200, {"message": "Success"}
    return 400, {"message": "Errror"}


def generate_doctors(request: HttpRequest) -> tuple[int, Message]:
    """Generate doctors for alghoritms."""
    if generate_random_data_for_doctors():
        return 200, {"message": "Success"}
    return 400, {"message": "Errror"}


def clear_all_data(request: HttpRequest) -> tuple[int, Message]:
    """Clear all data for alghoritms."""
    if remove_all_data():
        return 200, {"message": "Success"}
    return 400, {"message": "Errror"}
