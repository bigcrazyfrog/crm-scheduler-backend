from django.http import HttpRequest

from apps.core.api.schemas import Message
from apps.clients.api.schemas import ClientAdd, ClientOut

from ..models import Client


def all(
    request: HttpRequest,
) -> tuple[int, Message | ClientOut]:
    """Get a list of all existing clients."""
    clients = Client.objects.filter()
    return 200, list(clients)


def get(
    request: HttpRequest,
    client_id: str,
) -> tuple[int, Message | ClientOut]:
    """Get existing client."""
    client = Client.objects.filter(
        id=client_id,
    ).first()
    if client is None:
        return 404, {"message": "Client not found"}

    return 200, client


def add(
    request: HttpRequest,
    client_data: ClientAdd,
) -> tuple[int, Message | ClientOut]:
    """Add new client to database."""

    client = Client.objects.create(
        first_name=client_data.first_name,
        last_name=client_data.last_name,
        father_name=client_data.father_name,
        email=client_data.email,
    )

    return 201, client


def update(
    request: HttpRequest,
    client_id: str,
    client_data: ClientAdd,
) -> tuple[int, Message | ClientOut]:
    """Update existing client fields."""
    client = Client.objects.filter(id=client_id).first()

    client.first_name = client_data.first_name
    client.last_name = client_data.last_name
    client.father_name = client_data.father_name
    client.email = client_data.email

    client.save()

    return 200, client


def delete(
    request: HttpRequest,
    client_id: str,
) -> tuple[int, Message | ClientOut]:
    """Delete client from database."""
    client = Client.objects.filter(
        id=client_id,
    ).first()
    if client is None:
        return 404, {"message": "Client not found"}

    client.delete()
    return 200, {"message": "Successful delete"}
