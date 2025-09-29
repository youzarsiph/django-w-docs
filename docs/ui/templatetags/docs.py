"""docs Template tags"""

from django import template
from wagtail.models import Site

register = template.Library()


# Create your tags here.
@register.simple_tag(takes_context=True)
def get_site_root(context):
    """Get site root"""

    return Site.find_for_request(context["request"]).root_page.localized
