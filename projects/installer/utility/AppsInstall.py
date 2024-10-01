import logging
import subprocess
import importlib
from django.core import management
from django.urls import include, path
from drf_spectacular.generators import SchemaGenerator

from projects.installer.models import InstalledApp


def install(app_name):

    from config.settings.base import INSTALLED_APPS
    from config.urls import urlpatterns
    try:

        # Update the database
        obj, created = InstalledApp.objects.get_or_create(app_name=app_name)
        obj.is_installed = True
        obj.save()

        # # now I can generate the migrations for the new app
        management.call_command('makemigrations', app_name, interactive=False)
        # # and migrate it

        management.call_command('migrate', app_name, interactive=False)
        logging.info(f"{app_name} Installed Successfully")

        # Adding URL 
        try:
            app_urls = importlib.import_module(f'addons.apps.{app_name}.urls')
            urlpatterns.append(path(f'addons/apps/{app_name}/', include(app_urls), name=f"{app_name}"))
        except ImportError as e:
            print(f"Failed to import URLs for {app_name}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return True, f"{app_name} Installed Successfully"

    except Exception as e:
        logging.error(f"An error occurred while installing {app_name}. Reason: {e}")
        return False, f"Failed to install {app_name}"
