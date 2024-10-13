# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from addons.apps.project.models import Project
from addons.apps.project.rest_api.serializers import ProjectListSerializer, ProjectCreateSerializer
from rest_framework.decorators import action
from config.helpers.forms import FormsSerializers, LayoutSeralizers
import json
from config.helpers.Helpers import generate_fields, generate_customview_list, generate_customview
from config.helpers.Exception import exception
from dynamic_preferences.registries import global_preferences_registry
from config.helpers.Helpers import global_preferences


@extend_schema(tags=['Project'])
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer

    def list(self, request, *args, **kwargs):
        """
        Overridden method to add additional data to the response.
        It adds 'columns', 'customview_list', and 'customview' to the response data.

        Args:
            request: The request instance.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            The response with additional data.
        """

        response = super().list(request, *args, **kwargs)
        try:
            response.data['columns'] = generate_fields(
                'ProjectView', Project, includeactions=True)
            response.data['customview_list'] = generate_customview_list(1)
            response.data['customview'] = generate_customview(
                1, request.query_params.get('customview', None))
        except Exception as e:
            exception(e)
        return response

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Get the newly created object
        obj = Project.objects.get(pk=response.data['id'])

        # Check if non-project fields are present and add to projectattributes
        for key, value in request.data.items():
            if key not in [f.name for f in Project._meta.get_fields()]:
                obj.set_attribute(key, value, 'char')

        obj.save()
        return response

    @action(detail=False, methods=['get'])
    def forms(self, request, *args, **kwargs):
        # forms/get_form/?form_name=projects

        project_model = Project
        layoutdata = []

        # get form from dynamic preferences
        project_form = global_preferences['app_project__project_form']
        print("project_form", project_form.get('fields'))

        formser = LayoutSeralizers(data=project_form.get('fields'), many=True)
        formser.is_valid(raise_exception=True)
        return Response(formser.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
