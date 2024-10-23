from django.contrib import admin
from addons.apps.tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'created_by', 'assigned_to', 'created_at', 'updated_at')
    list_filter = ('status', 'created_by', 'assigned_to')
    search_fields = ('title', 'description')