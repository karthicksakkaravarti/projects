import subprocess

from django.apps import AppConfig, apps
from django.conf import settings

from config.helpers.Exception import exception


class InstallerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "projects.installer"

    # def ready(self):
    #     try:
    #         from .models import InstalledApp
    #         from .utility.AppsInstall import install

    #         for app in InstalledApp.objects.filter(is_installed=True):
    #             if app.app_name not in settings.INSTALLED_APPS:
    #                 # Modify settings in memory
    #                 settings.INSTALLED_APPS += ['apps.'+app.app_name]

    #                 # Clear the app registry
    #                 apps.app_configs = {}
    #                 apps.apps_ready = apps.models_ready = apps.loading = apps.ready = False

    #                 # Repopulate the app registry
    #                 apps.populate(settings.INSTALLED_APPS)

    #                 # Run makemigrations and migrate
    #                 subprocess.run(["python", "manage.py", "makemigrations"])
    #                 subprocess.run(["python", "manage.py", "migrate"])

    #     except Exception as e:
    #         exception(e)
    #         pass  # Table doesn't exist yet, skip this logic
