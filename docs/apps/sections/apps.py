"""AppConf for docs.apps.sections"""

from django.apps import AppConfig


# Create your AppConf here.
class DocsSectionsConfig(AppConfig):
    """App Configuration for docs.apps.sections"""

    label = "docs_sections"
    name = "docs.apps.sections"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        """Register signal receivers"""

        from docs.apps.signals import register_section_signal_receivers

        register_section_signal_receivers()
