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

A reusable documentation app powered by Python, Django, DRF and Wagtail CMS.

## Get started

Install the package:

```console
pip install django-w-docs
```

Configure your `Django` settings:

```python
# project/settings.py

# Application definition
INSTALLED_APPS = [
    "docs",
    "docs.api",  # Optional if you do not want to use the API
    "docs.apps.home",
    "docs.apps.indexes",
    "docs.apps.pages",
    "docs.apps.sections",
    "docs.apps.tags",
    "docs.cms",
    "docs.ui",
    # Deps
    "rest_wind",  # Optional if you do not want to use the API
    "rest_framework",  # Optional if you do not want to use the API
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
    ...
]
```

Run the migrations:

```console
# In your project root
python mange.py migrate
```

Update your `URLConf`:

```python
# project/urls.py

from django.urls import include, path


urlpatterns = [
    path("", include("docs.ui.urls")),
    path("api/", include("docs.api.urls")),  # Optional if you do not want to use the API
    path("api/", include("rest_framework.urls")),  # Optional if you do not want to use the API
    ...
    path("documents/", include(wagtaildocs_urls)),
    path("dashboard/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),  # Make sure this line is the last
]
```

## Key Features

- **CI/CD Pipelines**: Automated using GitHub Actions to ensure consistent and reliable deployment processes.
- **Dependency Management**: Powered by Poetry, a sophisticated tool for managing project dependencies with precision and reliability.
- **Code Formatting**: Automatically formatted with Black to maintain a consistent and readable codebase.
- **Code Linting**: Utilizes Ruff to identify and address potential issues early, enhancing code quality and maintainability.
- **Code Testing**: Utilizes Django to run tests.
- **Configuration Files**: Includes `.gitignore`, `pyproject.toml`, and other essential configuration files to streamline setup.

## Contributing

We warmly welcome contributions from the community. Please refer to our [CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to contribute effectively. Your feedback and participation are essential for the continued improvement of this template.

## Support

For inquiries or support, please open an issue or join the discussion in the [GitHub Discussions](https://github.com/youzarsiph/django-w-docs/discussions) section to engage with the community.

## Licensing

This project is licensed under the MIT License. A detailed copy of the terms can be found in the [LICENSE](LICENSE) file.
