from ninja import ModelSchema

from apps.cabinets.api.schemas import CabinetOut

from ..models import Doctor


class DoctorOut(ModelSchema):
    """Schema for output Doctor."""

    cabinets: list[CabinetOut] = []

    class Meta:
        model = Doctor
        fields = [
            "id",
            "first_name",
            "last_name",
            "father_name",
            "priority_cabinet",
            "cabinets",
        ]
