# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create new Django project and configure the settings
RUN django-admin startproject core
RUN cp -r docs core

# Configure settings
RUN echo "AUTH_USER_MODEL = 'users.User'" >> core/settings.py
RUN echo "INSTALLED_APPS += [" >> core/settings.py
RUN echo "    'docs'," >> core/settings.py
RUN echo "    'docs.apps.articles'," >> core/settings.py
RUN echo "    'docs.apps.blog'," >> core/settings.py
RUN echo "    'docs.apps.categories'," >> core/settings.py
RUN echo "    'docs.apps.home'," >> core/settings.py
RUN echo "    'docs.apps.links'," >> core/settings.py
RUN echo "    'docs.apps.tags'," >> core/settings.py
RUN echo "    'docs.apps.users'," >> core/settings.py
RUN echo "    'docs.cms'," >> core/settings.py
RUN echo "    'docs.ui'," >> core/settings.py
RUN echo "    'django_countries'," >> core/settings.py
RUN echo "    'phonenumber_field'," >> core/settings.py
RUN echo "    'django_filters'," >> core/settings.py
RUN echo "    'rest_wind'," >> core/settings.py
RUN echo "    'corsheaders'," >> core/settings.py
RUN echo "    'djoser'," >> core/settings.py
RUN echo "    'rest_framework'," >> core/settings.py
RUN echo "    'rest_framework.authtoken'," >> core/settings.py
RUN echo "    'wagtail_localize'," >> core/settings.py
RUN echo "    'wagtail_localize.locales'," >> core/settings.py
RUN echo "    'wagtail.contrib.frontend_cache'," >> core/settings.py
RUN echo "    'wagtail.contrib.search_promotions'," >> core/settings.py
RUN echo "    'wagtail.contrib.forms'," >> core/settings.py
RUN echo "    'wagtail.contrib.redirects'," >> core/settings.py
RUN echo "    'wagtail.embeds'," >> core/settings.py
RUN echo "    'wagtail.sites'," >> core/settings.py
RUN echo "    'wagtail.users'," >> core/settings.py
RUN echo "    'wagtail.snippets'," >> core/settings.py
RUN echo "    'wagtail.documents'," >> core/settings.py
RUN echo "    'wagtail.images'," >> core/settings.py
RUN echo "    'wagtail.search'," >> core/settings.py
RUN echo "    'wagtail.admin'," >> core/settings.py
RUN echo "    'wagtail_ai'," >> core/settings.py
RUN echo "    'wagtail'," >> core/settings.py
RUN echo "    'modelcluster'," >> core/settings.py
RUN echo "    'taggit'," >> core/settings.py
RUN echo "]" >> core/settings.py
RUN echo "MIDDLEWARE += ['wagtail.contrib.redirects.middleware.RedirectMiddleware']" >> core/settings.py

# Setup URLConf
RUN echo "from django.conf import settings" >> core/urls.py
RUN echo "from django.conf.urls.i18n import i18n_patterns" >> core/urls.py
RUN echo "from django.conf.urls.static import static" >> core/urls.py
RUN echo "from django.urls import include, re_path" >> core/urls.py
RUN echo "from wagtail import urls as wagtail_urls" >> core/urls.py
RUN echo "from wagtail.admin import urls as wagtailadmin_urls" >> core/urls.py
RUN echo "from wagtail.documents import urls as wagtaildocs_urls" >> core/urls.py
RUN echo "from wagtail.images.views.serve import ServeView" >> core/urls.py
RUN echo "urlpatterns += [" >> core/urls.py
RUN echo "    path('', include('django.conf.urls.i18n'))," >> core/urls.py
RUN echo "    re_path( r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve')," >> core/urls.py
RUN echo "] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)" >> core/urls.py
RUN echo "urlpatterns += i18n_patterns(" >> core/urls.py
RUN echo "    path('admin/', admin.site.urls)," >> core/urls.py
RUN echo "    path('api/', include('rest_framework.urls'))," >> core/urls.py
RUN echo "    path('api/', include('djoser.urls'))," >> core/urls.py
RUN echo "    path('api/', include('djoser.urls.authtoken'))," >> core/urls.py
RUN echo "    path('documents/', include(wagtaildocs_urls))," >> core/urls.py
RUN echo "    path('dashboard/', include(wagtailadmin_urls))," >> core/urls.py
RUN echo "    path('', include('django.contrib.auth.urls'))," >> core/urls.py
RUN echo "    path('api/', include('docs.api.urls'))," >> core/urls.py
RUN echo "    path('', include('docs.ui.urls', namespace='ui'))," >> core/urls.py
RUN echo "    path('', include(wagtail_urls))," >> core/urls.py
RUN echo ")" >> core/urls.py

# Run migrations
RUN cd core && python manage.py migrate


WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi"]
