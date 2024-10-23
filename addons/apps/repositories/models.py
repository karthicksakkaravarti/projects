# repositories/models.py

from django.db import models
import os

def repo_directory_path(instance, filename):
    # Repositories will be stored in MEDIA_ROOT/repositories/user_id/repo_name/
    return f'repositories/user_{instance.owner.id}/{instance.name}/{filename}'

class Repository(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    description = models.TextField(blank=True, verbose_name="Description")
    owner = models.ForeignKey('users.User', related_name='repositories', on_delete=models.CASCADE, verbose_name="Owner")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    repo_path = models.CharField(max_length=1024, editable=False, verbose_name="Repo Path")
    project = models.ForeignKey('project.Project', related_name='repositories', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Project")
    def save(self, *args, **kwargs):
        if not self.repo_path:
            self.repo_path = os.path.join('repositories', f'user_{self.owner.id}', self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
