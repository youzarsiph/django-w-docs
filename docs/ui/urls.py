"""Django Docs URLConf"""

from django.urls import path

from docs.ui.views import SearchView

# Create your URLConf here.
app_name = "docs"


urlpatterns = [
    path("search", SearchView.as_view(), name="search"),
]
