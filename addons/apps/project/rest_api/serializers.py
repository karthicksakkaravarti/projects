# serializers.py
from rest_framework import serializers
from addons.apps.project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'owner')
        read_only_fields = ('owner',)

