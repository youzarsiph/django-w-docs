"""AppConf for docs.apps.tags"""

from django.apps import AppConfig


# Create your config here.
class TagsConfig(AppConfig):
    """App configuration for docs.apps.tags"""

    label = "docs_tags"
    name = "docs.apps.tags"
    default_auto_field = "django.db.models.BigAutoField"
