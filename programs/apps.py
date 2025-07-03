from django.apps import AppConfig

# DO NOT import from .models here. This was the cause of the
# AppRegistryNotReady error, as it created a circular import loop
# when Django was starting up.

class ProgramsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'programs'
    verbose_name = "Programas de Eventos"