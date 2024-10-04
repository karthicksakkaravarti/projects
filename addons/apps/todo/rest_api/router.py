from rest_framework.routers import DefaultRouter
from addons.apps.todo.rest_api import viewset

todo_router = DefaultRouter()
todo_router.register(r'todos', viewset.TodoItemViewSet)