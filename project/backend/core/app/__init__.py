from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.core.app'
    verbose_name = 'core'
    label = 'core'

    # def ready(self):
    #     import backend.core.app.signals