# ruff: noqa
import importlib
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.mixins import LoginRequiredMixin
from config.settings.base import ADDONS_APPS
from projects.installer.rest_api import serializers as InstallerSerialisers
from rest_framework import serializers
from django.db.utils import ProgrammingError


class HomeView(LoginRequiredMixin, TemplateView):
    """Home view """
    template_name = 'index.html'

    def get(self, request, *args, **kwargs) :

        return super().get(request, *args, **kwargs)
    
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path("features/", TemplateView.as_view(template_name='pages/about.html'), name="features"),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("projects.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("", include("projects.installer.urls")),

    # ...
    # Media files
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("api/auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

# Automatically include URL patterns from all apps in the 'apps' folder
for app in os.listdir(ADDONS_APPS):
    if os.path.isdir(os.path.join(ADDONS_APPS, app)):
        try:

            info = importlib.import_module(f'addons.apps.{app}.info')
            serializer = InstallerSerialisers.ModuleImport(data=dict(info.module_info))
            if serializer.is_valid(raise_exception=True):
                app = serializer.save()
                if app.is_installed:
                    app_urls = importlib.import_module(f'addons.apps.{app.app_name}.urls')
                    urlpatterns.append(path(f'addons/apps/{app.app_name}/', include(app_urls)))
        except serializers.ValidationError as e:
            print(str(e))
            # Check for unique constraint violation and handle or ignore
            if 'app_name' in e.detail or 'unique' in str(e.detail['app_name'][0]):
                pass  # Ignore unique constraint error for app_name
            else:
                raise  # Re-raise any other validation errors           
        except ProgrammingError as e:
            # Handle the exception
            print(f"Database error: {e}")
        except ImportError as e:
            print(str(e))
            pass  # Module does not have a urls.py, skip it
        
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
