from django.urls import path, include
from addons.apps.tasks.rest_api.router import tasks_router

urlpatterns = [
    path('api/', include(tasks_router.urls)),
]