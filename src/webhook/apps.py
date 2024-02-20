from django.apps import AppConfig


class WebhookConfig(AppConfig):
    """
    AppConfig for the 'webhook' app.
    """
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "webhook"
