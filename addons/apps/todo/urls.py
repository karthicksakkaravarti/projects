from django.http import HttpResponse
from django.urls import path
from addons.apps.todo.rest_api.router import todo_router
from django.urls import path, include


def app_landing(request):
    return HttpResponse("Todo Successfully registered")


urlpatterns = [
    # Views
    path("", app_landing),
    path('api/', include(todo_router.urls)),
]
