from rest_framework.routers import DefaultRouter

from projects.installer.rest_api import viewset

installer_router = DefaultRouter()
installer_router.register(r'addons', viewset.InstalledAppViewSet)
