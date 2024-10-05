from rest_framework.routers import DefaultRouter
from .viewset import ProjectViewSet

project_router = DefaultRouter()
project_router.register(r'projects', ProjectViewSet)

# ... existing code ...