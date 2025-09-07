"""AppConf for docs.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for docs.cms"""

    name = "docs.cms"
    label = "docs_cms"
    default_auto_field = "django.db.models.BigAutoField"
