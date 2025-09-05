"""AppConf for docs.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for docs.api"""

    name = "docs.api"
    label = "docs_api"
    default_auto_field = "django.db.models.BigAutoField"
