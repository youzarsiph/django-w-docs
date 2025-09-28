"""Docs Index page"""

from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from docs.cms.blocks import MediaBlock


class AbstractDocsIndex(Page):
    """Abstract model for extension"""

    content = StreamField(
        MediaBlock(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )

    context_object_name = "index"
    parent_page_types = ["home.Home"]
    subpage_types = [
        "docs_sections.DocsSection",
        "docs_pages.DocsPage",
        "docs_pages.FromPage",
    ]

    api_fields = [APIField("content")]
    content_panels = Page.content_panels + [FieldPanel("content")]
    search_fields = Page.search_fields + [index.SearchField("content")]

    class Meta(Page.Meta):
        """Meta data"""

        abstract = True


class DocsIndex(AbstractDocsIndex):
    """Docs index pages"""

    template = "docs/index.html"
