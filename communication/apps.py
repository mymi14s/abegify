from django.apps import AppConfig


class CommunicationConfig(AppConfig):
    name = 'communication'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import communication.signals