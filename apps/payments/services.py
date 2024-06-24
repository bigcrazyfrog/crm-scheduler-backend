from datetime import datetime, timedelta

from yoomoney import Client, History, Quickpay

from config.settings import (
    MINIMUM_PAYMENT,
    RECIPIENT_ACCOUNT,
    SUBSCRIPTION_COST,
    YOOMONEY_TOKEN,
)

client = Client(YOOMONEY_TOKEN)


def get_user_transactions(user_id: str) -> History:
    """Get user transactions.

    Return user transactions from 7 days ago.

    """
    from_date = datetime.now() - timedelta(7)

    return client.operation_history(label=user_id, from_date=from_date)


def check_user_payment(user_id: str) -> bool:
    """Check transaction status.

    Return `True` if transaction is success, `False` otherwise.

    """
    transactions = get_user_transactions(user_id)
    for operation in transactions.operations:
        if (
            operation.status == "success" and
            operation.amount > MINIMUM_PAYMENT
        ):
            return True

    return False


def generate_payment(user_id: str) -> str:
    """Generate new payment.

    Return link to new payment.

    """
    quickpay = Quickpay(
        receiver=RECIPIENT_ACCOUNT,
        quickpay_form="shop",
        targets="Sponsor this project",
        paymentType="SB",
        label=user_id,
        sum=SUBSCRIPTION_COST,
    )
    return quickpay.base_url
