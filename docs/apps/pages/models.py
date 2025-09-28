"""Docs pages"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, Page
from wagtail.fields import StreamField
from wagtail.search import index

from docs.cms.blocks import AllBlocks


class AbstractDocsPage(Page):
    """Abstract model for extension"""

    description = models.CharField(
        max_length=256,
        verbose_name=_("description"),
        help_text=_("Page description"),
    )
    content = StreamField(
        AllBlocks(),
        verbose_name=_("content"),
        help_text=_("Page content"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="docs_tags.Tag",
        verbose_name=_("tags"),
        help_text=_("Tags"),
    )

    context_object_name = "page"
    parent_page_types = ["docs_indexes.DocsIndex", "docs_sections.DocsSection"]
    subpage_types = []

    api_fields = [APIField("description"), APIField("content"), APIField("tags")]
    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("tags"),
    ]
    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("content"),
        index.FilterField("tags"),
    ]

    class Meta(Page.Meta):
        """Meta data"""

        abstract = True


class DocsPage(AbstractDocsPage):
    """Docs pages"""

    template = "docs/page.html"


class FormField(AbstractFormField):
    job = ParentalKey(
        "docs_pages.FromPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class AbstractFromPage(AbstractEmailForm, AbstractDocsPage):
    """Base class for extension"""

    message = RichTextField(
        verbose_name=_("message"),
        help_text=_("Message to show after submitting form"),
    )
    tags = ClusterTaggableManager(
        blank=True,
        through="docs_tags.FromTag",
        verbose_name=_("tags"),
        help_text=_("Tags"),
    )

    parent_page_types = ["docs_indexes.DocsIndex", "docs_sections.DocsSection"]
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("tags"),
        MultiFieldPanel(
            [
                FieldPanel("subject"),
                FieldRowPanel([FieldPanel("from_address"), FieldPanel("to_address")]),
            ],
            _("Email"),
        ),
        InlinePanel("form_fields"),
        FieldPanel("message"),
    ]

    class Meta(Page.Meta):
        """Meta data"""

        abstract = True


class FromPage(AbstractFromPage):
    """From page"""

    template = "docs/form_page.html"
