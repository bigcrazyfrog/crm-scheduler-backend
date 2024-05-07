from django.http import HttpRequest

from apps.algorithm.services import shedule
from apps.core.api.schemas import Message


def v1(
    request: HttpRequest,
) -> tuple[int, Message]:
    """No coments... What is it???"""
    shedule()
    return 200, {"message": "Success"}
