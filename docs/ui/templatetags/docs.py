"""docs Template tags"""

from django import template
from django.shortcuts import resolve_url
from wagtail.models import Locale, Page, Site
from wagtail.templatetags.wagtailcore_tags import pageurl, slugurl

register = template.Library()


# Create your tags here.
@register.simple_tag(takes_context=True)
def page_url(context, page, language_code, fallback=None):
    """
    Outputs a page's URL as relative (/foo/bar/) if it's within the same site as the
    current page, or absolute (http://example.com/foo/bar/) if not.
    If kwargs contains a fallback view name and page is None, the fallback view url will be returned.
    """

    if page is None and fallback:
        return resolve_url(fallback)

    if not isinstance(page, Page):
        raise ValueError("pageurl tag expected a Page object, got %r" % page)

    try:
        trans = page.get_translation_or_none(
            Locale.objects.get(language_code=language_code)
        )

        if trans:
            return trans.get_url(request=context.get("request"))

    except Locale.DoesNotExist:
        return pageurl(context, page, fallback)

    return page.get_url(request=context.get("request"))


@register.simple_tag(takes_context=True)
def slug_url(context, slug, language_code):
    """
    Returns the URL for the page that has the given slug.

    First tries to find a page on the current site. If that fails or a request
    is not available in the context, then returns the URL for the first page
    that matches the slug on any site.
    """

    page = None

    try:
        site = Site.find_for_request(context["request"])
        current_site = site

    except KeyError:
        # No site object found - allow the fallback below to take place.
        pass

    else:
        if current_site is not None:
            page = (
                Page.objects.in_site(current_site)
                .filter(slug=slug, locale__language_code=language_code)
                .first()
            )

    # If no page is found, fall back to searching the whole tree.
    if page is None:
        page = Page.objects.filter(
            slug=slug, locale__language_code=language_code
        ).first()

    if page:
        # call page_url() instead of page.relative_url() here so we get the ``accepts_kwarg`` logic
        return page_url(context, page, language_code)

    else:
        return slugurl(context, slug)


@register.simple_tag(takes_context=True)
def get_site_root(context):
    """Get site root"""

    return Site.find_for_request(context["request"]).root_page
