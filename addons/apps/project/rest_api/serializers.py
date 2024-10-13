# serializers.py
from rest_framework import serializers
from addons.apps.project.models import Project

class ProjectListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'owner', 'status')

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'owner', 'status')
        read_only_fields = ('owner',)
