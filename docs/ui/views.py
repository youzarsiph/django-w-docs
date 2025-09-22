"""Django Docs views"""

from typing import Any

from django.views.generic import ListView
from wagtail.contrib.search_promotions.models import Query
from wagtail.models import Page


# Create your views here.
class SearchView(ListView):
    """Search View"""

    model = Page
    paginate_by = 25
    allow_empty = True
    allow_future = True
    queryset = Page.objects.live().public()
    template_name = "docs/search.html"
    context_object_name = "search_results"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        """Search new article"""

        return {
            **super().get_context_data(**kwargs),
            "search_query": self.request.GET.get("search", None),
            "search_results": self.get_search_results(),
        }

    def get_search_results(self):
        """Search pages and return results"""

        queryset = self.get_queryset()
        search_query = self.request.GET.get("search", None)

        search_results = queryset.none()

        if search_query:
            search_results = queryset.search(search_query)

            # Log the query so Wagtail can suggest promoted results
            Query.get(search_query).add_hit()

        return search_results
