from django.http import HttpResponse
from django.urls import path, include
from addons.apps.repositories.rest_api.router import repositories_router

def test(request):
    return HttpResponse("Success")


urlpatterns = [
    # Views
    path("api/", include(repositories_router.urls)),
]
