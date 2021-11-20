from django.apps import AppConfig
import os


class FampayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fampay'

    def ready(self):
        from .task import youtube_api_scheduler

        if os.environ.get('RUN_MAIN', None) != 'true':
            youtube_api_scheduler()
