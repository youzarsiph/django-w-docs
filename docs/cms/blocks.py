"""Custom blocks StreamField"""

from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail_blocks import blocks as w_blocks


# Create your blocks here.
class TextBlock(blocks.StreamBlock):
    """Custom StreamBlock for Text content"""

    quote = blocks.BlockQuoteBlock(help_text=_("Quote"))
    paragraph = blocks.RichTextBlock(help_text=_("Rich Text"))


class MediaBlock(TextBlock):
    """Custom StreamBlock for Text and Media content"""

    video = EmbedBlock(help_text=_("Video"))
    image = w_blocks.ImageBlock(help_text=_("Image"))
    document = DocumentChooserBlock(help_text=_("Document"))


class AllBlocks(MediaBlock):
    """All blocks included"""

    code = w_blocks.CodeBlock(help_text=_("Code"))
    accordion = w_blocks.AccordionBlock(help_text=_("Accordion"))
    alert = w_blocks.AlertBlock(help_text=_("Alert"))
    carousel = w_blocks.CarouselBlock(help_text=_("Carousel"))
    hover_gallery = w_blocks.HoverGalleryBlock(help_text=_("Hover gallery"))
    diff = w_blocks.DiffBlock(help_text=_("Diff"))
    fab = w_blocks.FABBlock(help_text=_("FAB"))
    list = w_blocks.ListBlock(help_text=_("List"))
    tabs = w_blocks.TabsBlock(help_text=_("Tabs"))
    steps = w_blocks.StepsBlock(help_text=_("Steps"))
    timeline = w_blocks.TimelineBlock(help_text=_("Timeline"))
    toast = w_blocks.ToastBlock(help_text=_("Toast"))
    browser = w_blocks.BrowserMockupBlock(help_text=_("Browser mockup"))
    code_mockup = w_blocks.CodeMockupBlock(help_text=_("Code mockup"))
    phone = w_blocks.PhoneMockupBlock(help_text=_("Phone mockup"))
