from worker.views.manager import create_cache
from django.db import models
from django.dispatch import receiver
from django.db.utils import OperationalError





@receiver(models.signals.class_prepared)
def hello(sender, **kwargs):
    try:
        from worker.views.manager import create_cache
        create_cache()
    except OperationalError:
        pass
    