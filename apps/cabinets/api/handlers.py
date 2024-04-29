from django.http import HttpRequest

from apps.cabinets.api.schemas import CabinetAdd, CabinetOut
from apps.cabinets.models import Cabinet
from apps.core.api.schemas import Message


def all(
    request: HttpRequest,
) -> tuple[int, Message | CabinetOut]:
    """Get a list of all existing cabinets."""
    cabinets = Cabinet.objects.filter()
    return 200, list(cabinets)


def add(
    request: HttpRequest,
    cabinet_data: CabinetAdd,
) -> tuple[int, Message | list[CabinetOut]]:
    """Add new cabinet to database."""
    cabinet = Cabinet.objects.create(
        title=cabinet_data.number,
        description=cabinet_data.description,
    )
    return 201, cabinet


def get(
    request: HttpRequest,
    cabinet_id: str,
) -> tuple[int, Message | CabinetOut]:
    """Get existing cabinet."""
    cabinet = Cabinet.objects.filter(
        id=cabinet_id,
    ).first()
    if cabinet is None:
        return 404, {"message": "Cabinet not found"}

    return 200, cabinet


def update(
    request: HttpRequest,
    cabinet_id: str,
    cabinet_data: CabinetAdd,
) -> tuple[int, Message | CabinetOut]:
    """Update existing cabinet fields."""
    cabinet = Cabinet.objects.filter(
        id=cabinet_id,
        author=request.user,
    ).first()
    if cabinet is None:
        return 404, {"message": "Quiz not found"}

    cabinet.title = cabinet_data.title
    cabinet.description = cabinet_data.description
    cabinet.save()

    return 200, cabinet


def delete(
    request: HttpRequest,
    cabinet_id: str,
) -> tuple[int, Message | CabinetOut]:
    """Delete cabinet from database."""
    cabinet = Cabinet.objects.filter(
        id=cabinet_id,
        author=request.user,
    ).first()
    if cabinet is None:
        return 404, {"message": "Quiz not found"}

    cabinet.delete()
    return 200, {"message": "Successful delete"}
