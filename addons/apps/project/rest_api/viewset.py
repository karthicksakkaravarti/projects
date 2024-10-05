# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from addons.apps.project.models import Project
from addons.apps.project.rest_api.serializers import ProjectSerializer
from rest_framework.decorators import action
from config.helpers.forms import FormsSerializers, LayoutSeralizers
import json
from config.helpers.Helpers import generate_fields, generate_customview_list, generate_customview
from config.helpers.Exception import exception
@extend_schema(tags=['Project'])
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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
            response.data['columns'] = generate_fields('ProjectView', Project, includeactions=True)
            response.data['customview_list'] = generate_customview_list(1)
            response.data['customview'] = generate_customview(1, request.query_params.get('customview', None))
        except Exception as e:
            exception(e)
        return response
    
    @action(detail=False, methods=['get'])
    def forms(self, request, *args, **kwargs):
        # forms/get_form/?form_name=projects

        project_model = Project
        layoutdata = []

        for field in project_model._meta.get_fields():
            # Skip relational fields
            if field.is_relation:
                continue

            field_info = {
                "name": field.verbose_name.title(),
                "fieldtype": self.get_field_type(field),
                "sm": "12",
                "valuelist": self.get_valuelist(field),
                "value": "",  # You can set default values here if needed
                "dbfield": field.name,
                "required": not field.blank,
            }
            layoutdata.append(field_info)

        formser = LayoutSeralizers(data=layoutdata, many=True)
        formser.is_valid(raise_exception=True)
        return Response(formser.data)

    def get_field_type(self, field):
        field_mapping = {
            'CharField': 'TextField',
            'TextField': 'TextArea',
            'IntegerField': 'NumberField',
            'FloatField': 'NumberField',
            'BooleanField': 'Checkbox',
            'DateField': 'DateField',
            'DateTimeField': 'DateTimePicker',
            # Add more mappings as needed
        }
        return field_mapping.get(field.get_internal_type(), 'TextField')

    def get_valuelist(self, field):
        if field.choices:
            return [{"value": choice[0], "display": choice[1]} for choice in field.choices]
        return []
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

