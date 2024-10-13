from django.http import HttpResponse
from django.urls import path, include
from addons.apps.documents.rest_api.router import documents_router



urlpatterns = [
    # Views
    path('api/', include(documents_router.urls)),
]
