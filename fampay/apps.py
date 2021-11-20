from django.apps import AppConfig
import os


class FampayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fampay'

    # Below code will only run once when the server is started
    def ready(self):
        """
        This method initializes the thread for calling youtube api
        """
        from .task import youtube_api_scheduler

        if os.environ.get('RUN_MAIN', None) != 'true':
            youtube_api_scheduler()
