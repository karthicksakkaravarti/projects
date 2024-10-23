from rest_framework import routers
from addons.apps.tasks.rest_api.viewset import TaskViewSet

tasks_router = routers.DefaultRouter()
tasks_router.register(r'tasks', TaskViewSet)