import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celerymails.settings")

app = Celery("celerymails")

app.conf.broker_url = "redis://localhost:6379/0"
app.config_from_object(
    "django.conf:settings", namespace="CELERY"
)  # Will look for settings with CELERY_ prefix
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

