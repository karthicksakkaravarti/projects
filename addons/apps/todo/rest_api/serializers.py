# serializers.py
from rest_framework import serializers
from addons.apps.todo.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'completed')
