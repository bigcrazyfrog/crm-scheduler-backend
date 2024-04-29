from ninja import ModelSchema

from ..models import Cabinet


class CabinetAdd(ModelSchema):
    """Schema for new cabinet."""

    class Meta:
        model = Cabinet
        fields = ["number", "description"]


class CabinetOut(ModelSchema):
    """Schema for output cabinet."""

    class Meta:
        model = Cabinet
        fields = ["id", "number", "description"]
