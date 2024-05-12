from django.http import HttpRequest

from apps.algorithm.services import make_schedule, make_schedule_v2
from apps.core.api.schemas import Message
from apps.doctors.models import Doctor
from apps.intervals.models import Interval


def clear_cabinets(request: HttpRequest) -> tuple[int, Message]:
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
    """v2 for alghoritms"""
    doctors = Doctor.objects.prefetch_related("cabinets")
    intervals = Interval.objects.all().select_related("cabinet", "doctor")

    make_schedule_v2(doctors, intervals)
    return 200, {"message": "Success"}
