from django.http import HttpResponse
from django.urls import path
from addons.apps.project.rest_api.router import project_router
from django.urls import path, include
from . import views

def app_landing(request):
    return HttpResponse("Project Successfully registered")


urlpatterns = [
    # Views
    path("", app_landing),
    path('api/', include(project_router.urls)),
    path('project/<int:project_id>/add-field/', views.add_dynamic_field, name='add_dynamic_field'),

]
