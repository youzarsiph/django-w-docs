"""AppConf for docs.apps.pages"""

from django.apps import AppConfig


# Create your AppConf here.
class DocsPagesConfig(AppConfig):
    """App Configuration for docs.apps.pages"""

    label = "docs_pages"
    name = "docs.apps.pages"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        """Register signal receivers"""

        from docs.apps.signals import register_page_signal_receivers

        register_page_signal_receivers()
