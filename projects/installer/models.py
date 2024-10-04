# models.py

from django.db import models
from django.db.models import JSONField

class InstalledApp(models.Model):
    app_name = models.CharField(max_length=255, unique=True, verbose_name="Addons Name")
    is_installed = models.BooleanField(default=False, verbose_name="Status")
    category = models.CharField(max_length=200, null=True, verbose_name="Category")
    version = models.CharField(max_length=100, verbose_name="Version")
    author = models.CharField(max_length=200, verbose_name="Author")
    other = JSONField(verbose_name="Others", null=True)