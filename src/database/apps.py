from django.apps import AppConfig


class DatabaseConfig(AppConfig):
    """
    Configuration class for the 'database' app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "database"
