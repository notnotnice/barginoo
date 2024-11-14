from src.apps_config import CleanAppConfig


class AccountConfig(CleanAppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
