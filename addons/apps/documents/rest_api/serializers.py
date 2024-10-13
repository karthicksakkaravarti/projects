# docs/serializers.py

from rest_framework import serializers
from addons.apps.documents.models import Document, Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    category = serializers.CharField()
    class Meta:
        model = Document
        fields = ['id', 'title', 'content', 'category', 'created_by', 'created_at', 'updated_at', 'project']

