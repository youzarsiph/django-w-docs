"""Docs Section page"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from docs.cms.blocks import MediaBlock


class AbstractDocsSection(Page):
    """Abstract model for extension"""

    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Page description"),
    )
    content = StreamField(
        MediaBlock(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "section"
    parent_page_types = ["indexes.DocsIndex", "sections.DocsSection"]
    subpage_types = ["pages.DocsPage", "sections.DocsSection"]

    api_fields = [APIField("description"), APIField("content")]
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("content"),
    ]

    class Meta(Page.Meta):
        """Meta data"""

        abstract = True
        verbose_name = _("Docs sections")
        verbose_name_plural = _("Docs sections")


class DocsSection(AbstractDocsSection):
    """Docs section pages"""

    template = "docs/section.html"
