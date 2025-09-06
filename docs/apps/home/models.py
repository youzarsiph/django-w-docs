"""Home page"""

from wagtail.models import Page


class Home(Page):
    """Home page"""

    template = "docs/base.html"
    context_object_name = "home"
    parent_page_types = ["wagtailcore.Page"]
