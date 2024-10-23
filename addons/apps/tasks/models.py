from django.db import models
from django.contrib.auth.models import User
import uuid

class Task(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,  verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    due_date = models.DateField(null=True, blank=True, verbose_name="Due Date")
    created_by = models.ForeignKey('users.User', related_name='tasks_created', on_delete=models.CASCADE, verbose_name="Created By")
    assigned_to = models.ForeignKey('users.User', related_name='tasks_assigned', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Assigned To")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    project = models.ForeignKey('project.Project', related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title