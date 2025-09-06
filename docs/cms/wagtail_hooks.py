"""Wagtail Hooks used to customize the view-level behavior of the Wagtail admin and front-end"""

from django.utils.translation import gettext_lazy as _
from taggit.models import Tag
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


class TagsSnippetViewSet(SnippetViewSet):
    """
    This will allow you to have a tag admin interface within the main
    menu in which you can add, edit or delete your tags.
    """

    panels = [FieldPanel("name")]
    model = Tag
    icon = "tag"
    add_to_admin_menu = True
    menu_label = _("Tags")
    menu_order = 200
    list_display = ["name", "slug"]
    search_fields = ("name",)


register_snippet(TagsSnippetViewSet)
