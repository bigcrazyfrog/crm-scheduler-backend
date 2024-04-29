from django.http import HttpRequest

from apps.core.api.schemas import Message
from apps.doctors.api.schemas import DoctorOut

from ..models import Doctor


def all(
    request: HttpRequest,
) -> tuple[int, Message | DoctorOut]:
    """Get a list of all existing doctors."""
    doctors = Doctor.objects.filter()
    return 200, list(doctors)


def get(
    request: HttpRequest,
    doctor_id: str,
) -> tuple[int, Message | DoctorOut]:
    """Get existing doctor."""
    doctor = Doctor.objects.filter(
        id=doctor_id,
    ).first()
    if doctor is None:
        return 404, {"message": "Doctor not found"}

    return 200, doctor


def delete(
    request: HttpRequest,
    doctor_id: str,
) -> tuple[int, Message | DoctorOut]:
    """Delete doctor from database."""
    doctor = Doctor.objects.filter(
        id=doctor_id,
    ).first()
    if doctor is None:
        return 404, {"message": "Doctor not found"}

    doctor.delete()
    return 200, {"message": "Successful delete"}
