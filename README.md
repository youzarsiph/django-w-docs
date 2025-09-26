# django-w-docs

[![CI](https://github.com/youzarsiph/django-w-docs/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/django-w-docs/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/django-w-docs/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/django-w-docs/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/django-w-docs/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/django-w-docs/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/django-w-docs/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/django-w-docs/actions/workflows/ruff.yml)
[![Docker Image](https://github.com/youzarsiph/django-w-docs/actions/workflows/docker-image.yml/badge.svg)](https://github.com/youzarsiph/django-w-docs/actions/workflows/docker-image.yml)
[![Docker Publish](https://github.com/youzarsiph/django-w-docs/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/youzarsiph/django-w-docs/actions/workflows/docker-publish.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/django-w-docs?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-docs/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-w-docs?logo=python&logoColor=white)](https://pypi.org/project/django-w-docs/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-w-docs?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-docs/)
[![PyPI - License](https://img.shields.io/pypi/l/django-w-docs?logo=pypi&logoColor=white)](https://pypi.org/project/django-w-docs/)

## Overview

**django-w-docs** is a reusable, production-ready documentation application built with Python, Django, Django REST Framework, and Wagtail CMS, styled with Tailwind CSS and daisyUI. It comes with sensible defaults, modern theming, and clean APIs—helping you launch structured, searchable documentation quickly and scale it with confidence.

---

## Demo

[![Demo](https://img.youtube.com/vi/Ex1O9G6j2-M/maxresdefault.jpg)](https://youtu.be/Ex1O9G6j2-M)

---

## Key features

- **Full CMS:** Wagtail-powered editorial interface with pages, media, search, and governance.  
- **Modern UI:** Utility-first styling with Tailwind CSS for responsive, accessible layouts.  
- **Theming:** All daisyUI themes included, with support for custom themes.  
- **API ready:** Optional REST API endpoints for headless delivery and integrations.  
- **CI/CD:** GitHub Actions pipelines for automated testing, linting, and deployment.  
- **Dependencies:** Managed with Poetry for reproducibility and clarity.  
- **Formatting:** Black for consistent, automatic code formatting.  
- **Linting:** Ruff for fast, comprehensive linting.  
- **Testing:** Django test runner for unit and integration tests.  
- **Starter configs:** `.gitignore`, `pyproject.toml`, and other boilerplate included.

---

## Use cases

- **Product docs & API reference:** Guides, FAQs, and endpoint documentation with search and tags.  
- **Knowledge base:** Self‑serve help center to reduce support load.  
- **Internal handbook:** Onboarding, SOPs, and runbooks with role‑based access.  
- **Release notes & policies:** Publish updates, policies, and compliance docs.  
- **Multilingual content:** Maintain parity across languages with Wagtail i18n.  
- **In‑product help:** Surface contextual docs via the REST API.  

---

## Installation

```bash
pip install django-w-docs
```

---

## Configuration

### Add installed apps

```python
# project/settings.py

INSTALLED_APPS = [
    "docs",
    "docs.api",              # Optional: REST API
    "docs.apps.home",        # Optional: if your project includes a Home model ('home.Home')
    "docs.apps.indexes",
    "docs.apps.pages",
    "docs.apps.sections",
    "docs.apps.tags",
    "docs.cms",
    "docs.ui",

    # Dependencies
    "rest_wind",             # Optional: REST API
    "rest_framework",        # Optional: REST API
    "wagtail_blocks",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    # ...
]
```

### Run migrations

```bash
python manage.py migrate
```

### Update URL configuration

```python
# project/urls.py

from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("", include("docs.ui.urls")),
    path("api/", include("docs.api.urls")),           # Optional: REST API
    path("api/", include("rest_framework.urls")),     # Optional: REST API
    # ...
    path("documents/", include(wagtaildocs_urls)),
    path("dashboard/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),                  # Keep this last
]
```

---

## Theming and templates

All templates in django-w-docs extend `docs/base.html`. Create and customize this base template to match your brand.

### Create the template directory

```bash
mkdir -p your_app/templates/docs
```

### Create the base template

```bash
touch your_app/templates/docs/base.html
```

You can extend `docs/base.html` in your own templates or override any provided template for full control.

### Available blocks and context

- **`docs/base.html`**  
  - **Blocks:** `theme`, `toggle_theme`, `head`, `title`, `styles`, `navbar`, `branding`, `navbar_center`, `navbar_end`, `content`, `footer`, `drawer_branding`, `drawer_content`  
  - **Context:** `home` (site root page)

- **`docs/index.html`**  
  - **Blocks:** All from `docs/base.html`  
  - **Context:** `index` (docs index page)

- **`docs/section.html`**  
  - **Blocks:** All from `docs/base.html`  
  - **Context:** `section` (DocsSection instance)

- **`docs/page.html`**  
  - **Blocks:** All from `docs/base.html`  
  - **Context:** `page` (DocsPage instance)

- **`docs/search.html`**  
  - **Blocks:** All from `docs/base.html`  
  - **Context:** `search_results` (`PageQuerySet` results)

---

## Contributing

We welcome contributions from the community. Please review the [CONTRIBUTING](CONTRIBUTING.md) guide for setup, coding standards, and workflow. Opening an issue before major changes helps align on scope and direction.

---

## Support

For questions, bug reports, or feature requests, open an issue or join the conversation in [GitHub Discussions](https://github.com/youzarsiph/django-w-docs/discussions).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
