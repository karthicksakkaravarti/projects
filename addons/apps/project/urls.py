from django.http import HttpResponse
from django.urls import path
from addons.apps.project.rest_api.router import project_router
from django.urls import path, include


def app_landing(request):
    return HttpResponse("Project Successfully registered")


urlpatterns = [
    # Views
    path("", app_landing),
    path('api/', include(project_router.urls)),
]
