import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')

app = Celery('scheduler')

app.config_from_object('django.conf:settings', namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': { 
        'task': '<name_of_app>.tasks.repeat_order_make',
        'schedule': crontab(minute=5),
    }
}