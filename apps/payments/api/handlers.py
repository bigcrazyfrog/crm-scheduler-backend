from django.http import HttpRequest

from apps.core.api.schemas import DefaultResponse
from apps.payments.services import check_user_payment, generate_payment


def check_payment(
    request: HttpRequest,
) -> tuple[int, DefaultResponse]:
    """Check successful transactions."""
    user = request.user
    if check_user_payment(user.id):
        if not user.is_premium:
            user.is_premium = True
            user.save()
        return 200, DefaultResponse(
            message="Successful payment",
        )

    return 200, DefaultResponse(
        status="rejected",
        message="The money didn't arrive",
    )


def get_pay_link(
    request: HttpRequest,
) -> tuple[int, DefaultResponse]:
    """Get lint for quick payment."""
    link = generate_payment(request.user.id)
    return 200, DefaultResponse(message=link)
