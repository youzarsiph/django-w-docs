"""AppConf for docs.apps.docs"""

from django.apps import AppConfig


# Create your AppConf here.
class ArticlesConfig(AppConfig):
    """App Configuration for docs.apps.docs"""

    name = "docs.apps.docs"
    default_auto_field = "django.db.models.BigAutoField"
