import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings.dev')

celery = Celery('home')
celery.config_from_object('django.conf:settings', namespace='CELERY')
