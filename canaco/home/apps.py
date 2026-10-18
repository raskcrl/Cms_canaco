from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # Comenta o elimina esta línea si no tienes un archivo signals.py
        # import home.signals
        pass