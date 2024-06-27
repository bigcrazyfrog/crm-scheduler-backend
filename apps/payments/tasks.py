from django.contrib.auth import get_user_model

from config import celery_app
from config.settings import MINIMUM_PAYMENT

from apps.payments.services import get_user_transactions


@celery_app.task
def check_payments():
    """Check payments from users.

    Check transactions from 7 days ago and update user status.

    """
    transactions = get_user_transactions()
    for operation in transactions.operations:
        labels = []
        if (
            operation.status == "success" and
            operation.amount > MINIMUM_PAYMENT
        ):
            labels.append(operation.label)

    users = get_user_model().objects.filter(id__in=labels)
    users.update(is_premium=True)
