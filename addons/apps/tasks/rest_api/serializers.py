from rest_framework import serializers
from addons.apps.tasks.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.CharField( source='get_status_display')
    # assigned_to = serializers.PrimaryKeyRelatedField(
    #     queryset=User.objects.all(),
    #     required=False,
    #     allow_null=True
    # )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_by', 'assigned_to', 'created_at', 'updated_at', 'project']