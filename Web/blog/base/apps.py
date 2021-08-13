from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    # override the name of the base app in the admin page.
    verbose_name = 'Blog'
