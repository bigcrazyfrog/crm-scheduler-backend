from ninja import ModelSchema

from ..models import Schedule


class ScheduleAdd(ModelSchema):
    """Schema for newSchedule."""

    class Meta:
        model = Schedule
        fields = ["name", "description"]


class ScheduleOut(ModelSchema):
    """Schema for output Schedule."""

    class Meta:
        model = Schedule
        fields = ["id", "name", "description"]
