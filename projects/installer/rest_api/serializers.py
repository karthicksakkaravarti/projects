# serializers.py
import os

from rest_framework import serializers

from config.settings import base
from projects.installer.models import InstalledApp

from rest_framework import serializers

from django.core.validators import RegexValidator
from rest_framework import serializers


# Navigation serializer
class NavigationItemSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    icon = serializers.CharField(max_length=255)
    to = serializers.CharField(max_length=255)


# Main serializer
class ModuleImport(serializers.ModelSerializer):
    navigation = NavigationItemSerializer(many=True)
    app_name = serializers.CharField()
 
    class Meta:
        model = InstalledApp
        exclude = ['other']  # exclude the other field, we will handle it manually

    def validate_version(self, value):
        # Validating standard versioning pattern
        validator = RegexValidator(r'^(\d+\.)?(\d+\.)?(\d+)$')
        validator(value)
        return value

    def create(self, validated_data):
        try:
            navigation_data = validated_data.pop('navigation', None)
            # Using get_or_create based on the app_name field
            instance, created = InstalledApp.objects.get_or_create(
                app_name=validated_data['app_name'],
                defaults=validated_data
            )

            # If the object was not created, it means it already existed, so we update it
            if not created:
                for attr, value in validated_data.items():
                    setattr(instance, attr, value)
                instance.save()

            if navigation_data:
                instance.other = {"navigation": navigation_data}
                instance.save()

            return instance
        except serializers.ValidationError as e:
            print(str(e))
            # Check for unique constraint violation and handle or ignore
            if 'app_name' in e.detail and 'unique' in str(e.detail['app_name'][0]):
                pass  # Ignore unique constraint error for app_name
            else:
                raise  # Re-raise

class InstalledAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalledApp
        fields = '__all__'


class AppInstallSerializer(serializers.ModelSerializer):
    app_name = serializers.CharField(
        max_length=255,
        help_text='The name of the Django app you want to install.'
    )

    def validate_app_name(self, value):
        app_path = os.path.join(base.BASE_DIR, 'addons/apps',
                                value)
        try:
            # Check if the directory exists
            if not os.path.exists(app_path):
                raise serializers.ValidationError("App does not exist in the apps directory.")

            if InstalledApp.objects.filter(app_name=value, is_installed=True).exists():
                raise serializers.ValidationError("App Already installed")

            # Try importing the app's urls.py to see if it's a valid Python package
        except ImportError:
            raise serializers.ValidationError("App does not exist or urls.py is missing.")
        return value

    is_installed = serializers.BooleanField(read_only=True)

    class Meta:
        model = InstalledApp
        fields = ['app_name', 'is_installed']
