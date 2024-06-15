from django.http import HttpRequest

from apps.cabinets.models import Cabinet
from apps.core.api.schemas import Message
from apps.doctors.api.schemas import DoctorAdd, DoctorOut

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


def add(
    request: HttpRequest,
    doctor_data: DoctorAdd,
) -> tuple[int, Message | DoctorOut]:
    """Add new doctor to database."""
    priority_cabinet = Cabinet.objects.filter(
        id=doctor_data.priority_cabinet,
    ).first()
    if priority_cabinet is None:
        return 404, {"message": "Priority cabinet not found"}

    doctor = Doctor.objects.create(
        first_name=doctor_data.first_name,
        last_name=doctor_data.last_name,
        father_name=doctor_data.father_name,
        priority_cabinet=priority_cabinet,
    )

    for cabinet in doctor_data.cabinets:
        new_cabinet = Cabinet.objects.filter(id=cabinet).first()
        if new_cabinet is not None:
            doctor.cabinets.add(new_cabinet)

    return 201, doctor


def update(
    request: HttpRequest,
    doctor_id: str,
    doctor_data: DoctorAdd,
) -> tuple[int, Message | DoctorOut]:
    """Update existing doctor fields."""
    doctor = Doctor.objects.filter(id=doctor_id).first()

    priority_cabinet = Cabinet.objects.filter(
        id=doctor_data.priority_cabinet,
    ).first()
    if priority_cabinet is None:
        return 404, {"message": "Priority cabinet not found"}

    doctor.first_name = doctor_data.first_name
    doctor.last_name = doctor_data.last_name
    doctor.father_name = doctor_data.father_name
    doctor.priority_cabinet = priority_cabinet

    doctor.cabinets.clear()
    for cabinet in doctor_data.cabinets:
        new_cabinet = Cabinet.objects.filter(id=cabinet).first()
        if new_cabinet is not None:
            doctor.cabinets.add(new_cabinet)

    doctor.save()

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
