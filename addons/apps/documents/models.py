# docs/models.py

from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='documents', on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey('users.User', related_name='documents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('project.Project', related_name='documents', on_delete=models.CASCADE, null=True, blank=True)
    # Optional: Add versioning, tags, etc.

    def __str__(self):
        return self.title
