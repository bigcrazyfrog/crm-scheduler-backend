from ninja import ModelSchema

from ..models import Client


class ClientOut(ModelSchema):
    """Schema for output Client."""

    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "father_name",
            "email",
        ]


class ClientAdd(ModelSchema):
    """Schema for input Client."""

    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "father_name",
            "email",
        ]
