"""Signals to invalidate index pages"""

from django.db.models.signals import pre_delete
from wagtail.contrib.frontend_cache.utils import PurgeBatch
from wagtail.signals import page_published

from docs.apps.pages.models import DocsPage
from docs.apps.sections.models import DocsSection


def invalidate_index(sender, **kwargs):
    """Invalidate index page to reflect the changes in children"""

    batch = PurgeBatch()
    batch.add_page(kwargs["instance"])
    batch.purge()


def register_signal_receivers(sender):
    """Register signal receivers"""

    pre_delete.connect(invalidate_index, sender=sender)
    page_published.connect(invalidate_index, sender=sender)


def register_section_signal_receivers():
    register_signal_receivers(DocsSection)


def register_page_signal_receivers():
    register_signal_receivers(DocsPage)
