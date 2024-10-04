# urls.py

from django.urls import include, path

from projects.installer.rest_api import router

urlpatterns = [
    path('api/', include(router.installer_router.urls)),
    # ... other url patterns
]
