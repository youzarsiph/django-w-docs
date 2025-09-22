"""AppConf for docs"""

from django.apps import AppConfig


# Create your AppConf here.
class ArticlesConfig(AppConfig):
    """App Configuration for docs"""

    name = "docs"
    default_auto_field = "django.db.models.BigAutoField"
