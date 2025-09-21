"""AppConf for docs.ui"""

from django.apps import AppConfig


# Create your config here.
class DocsUIConfig(AppConfig):
    """App configuration for docs.ui"""

    name = "docs.ui"
    label = "docs_ui"
    default_auto_field = "django.db.models.BigAutoField"
