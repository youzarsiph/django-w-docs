"""Custom blocks StreamField"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock
from wagtail_blocks import blocks as wagtail_blocks


# Create your blocks here.
class TextBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    quote = blocks.BlockQuoteBlock(help_text=_("Quote"))
    paragraph = blocks.RichTextBlock(help_text=_("Rich Text"))


class MediaBlock(TextBlock):
    """Custom StreamBlock for Text and Media content"""

    video = EmbedBlock(help_text=_("Video"))
    image = ImageBlock(help_text=_("Image"))
    document = DocumentChooserBlock(help_text=_("Document"))


class AllBlocks(MediaBlock):
    """All blocks included"""

    code = wagtail_blocks.CodeBlock(help_text=_("Code"))
    accordion = wagtail_blocks.AccordionBlock(help_text=_("Accordion"))
    alert = wagtail_blocks.AlertBlock(help_text=_("Alert"))
    carousel = wagtail_blocks.CarouselBlock(help_text=_("Carousel"))
    diff = wagtail_blocks.DiffBlock(help_text=_("Diff"))
    fab = wagtail_blocks.FABBlock(help_text=_("FAB"))
    list = wagtail_blocks.ListBlock(help_text=_("List"))
    tabs = wagtail_blocks.TabsBlock(help_text=_("Tabs"))
    steps = wagtail_blocks.StepsBlock(help_text=_("Steps"))
    timeline = wagtail_blocks.TimelineBlock(help_text=_("Timeline"))
    toast = wagtail_blocks.ToastBlock(help_text=_("Toast"))
    browser = wagtail_blocks.BrowserMockupBlock(help_text=_("Browser mockup"))
    code_mockup = wagtail_blocks.CodeMockupBlock(help_text=_("Code mockup"))
    phone = wagtail_blocks.PhoneMockupBlock(help_text=_("Phone mockup"))
