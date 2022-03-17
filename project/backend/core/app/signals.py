# from worker.views.manager import create_cache
from django.db import models
from django.dispatch import receiver


@receiver(models.signals.class_prepared)
def hello(sender, **kwargs):
    from worker.views.manager import create_cache
    create_cache()
    