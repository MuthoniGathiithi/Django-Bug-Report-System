from django.apps import AppConfig

class BugsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bugs'

    def ready(self):
        import bugs.signals
