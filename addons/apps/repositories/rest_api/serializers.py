# repositories/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from addons.apps.repositories.models import Repository

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RepositorySerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)
    class Meta:
        model = Repository
        fields = ['id', 'name', 'description', 'created_at', 'repo_path', 'project']

class FileSerializer(serializers.Serializer):
    file_path = serializers.CharField(max_length=1024)
    content = serializers.CharField()
