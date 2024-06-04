from ninja import ModelSchema

from apps.cabinets.api.schemas import CabinetOut
from apps.doctors.api.schemas import DoctorOut
from apps.schedule.api.schemas import ScheduleAdd

from ..models import Interval


class IntervalAdd(ModelSchema):
    """Schema for new Interval."""

    class Meta:
        model = Interval
        fields = ["start", "end", "doctor", "schedule"]


class IntervalOut(ModelSchema):
    """Schema for output Interval."""

    doctor: DoctorOut
    schedule: ScheduleAdd
    cabinet: CabinetOut | None

    class Meta:
        model = Interval
        fields = ["start", "end"]
