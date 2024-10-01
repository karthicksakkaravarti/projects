# views.py
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import filters, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from projects.installer.models import InstalledApp
from projects.installer.rest_api.serializers import AppInstallSerializer, InstalledAppSerializer, NavigationItemSerializer
from projects.installer.utility.AppsInstall import install
from config.helpers.mixins import ColumnsMixin

class InstalledAppViewSet(ColumnsMixin, GenericViewSet, mixins.ListModelMixin ):
    queryset = InstalledApp.objects.all()
    serializer_class = InstalledAppSerializer
    list_model = InstalledApp
    include_actions = True

    @action(detail=False, methods=['POST'], serializer_class=AppInstallSerializer)
    def install(self, request):
        serializer = AppInstallSerializer(data=request.data)
        if serializer.is_valid():
            app_name = serializer.validated_data['app_name']
            app, created = InstalledApp.objects.get_or_create(app_name=app_name)

            if not app.is_installed:
                success, message = install(app_name)
                app.is_installed = success
                app.save()

            if success:
                return Response({"detail": message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"detail": message}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def navigation(self, request):
        try:
            apps = InstalledApp.objects.filter(is_installed=True)
            navigation_items = []
            for app in apps:
                navigation = app.other.get('navigation', [])
                navigation_items.extend(navigation)
            serializer = NavigationItemSerializer(navigation_items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
