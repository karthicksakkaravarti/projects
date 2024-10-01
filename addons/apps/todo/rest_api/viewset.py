# views.py
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from addons.apps.todo.models import TodoItem
from .serializers import TodoItemSerializer



@extend_schema(tags=['Todo'])
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

