"""Data Models for docs.apps.tags"""

from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class Tag(TaggedItemBase):
    """Through model for defining m2m rel between Pages and Tags"""

    content_object = ParentalKey(
        "docs_pages.DocsPage",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )


class FromTag(TaggedItemBase):
    """Through model for defining m2m rel between FromPages and Tags"""

    content_object = ParentalKey(
        "docs_pages.FromPage",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )
