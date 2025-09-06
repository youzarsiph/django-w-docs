"""AppConf for docs.apps.indexes"""

from django.apps import AppConfig


# Create your AppConf here.
class DocsIndexConfig(AppConfig):
    """App Configuration for docs.apps.indexes"""

    label = "docs_indexes"
    name = "docs.apps.indexes"
    default_auto_field = "django.db.models.BigAutoField"
