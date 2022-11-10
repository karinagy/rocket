from celery import Celery

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rocketdata_test.settings')

app = Celery('rocketdata_test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
