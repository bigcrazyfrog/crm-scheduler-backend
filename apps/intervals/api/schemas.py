from ninja import ModelSchema

from apps.cabinets.api.schemas import CabinetOut
from apps.doctors.api.schemas import DoctorOut

from ..models import Interval


class IntervalAdd(ModelSchema):
    """Schema for new Interval."""

    class Meta:
        model = Interval
        fields = ["start", "end", "doctor"]


class IntervalOut(ModelSchema):
    """Schema for output Interval."""

    doctor: DoctorOut
    cabinet: CabinetOut | None

    class Meta:
        model = Interval
        fields = ["start", "end"]
