import os
from celery import Celery, current_task

os.environ['DJANGO_SETTINGS_MODULE'] = '<PROJECT_NAME>.settings'

app = Celery('<APP_NAME>', broker='amqp://<CELERY_USER>:<CELERY_PASS>@localhost:5672/<CELERY_VHOST>')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


