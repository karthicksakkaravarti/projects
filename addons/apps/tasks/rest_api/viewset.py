from rest_framework import viewsets, permissions
from addons.apps.tasks.models import Task
from addons.apps.tasks.rest_api.serializers import TaskSerializer
from config.helpers.forms import FormsSerializers, LayoutSeralizers
from config.helpers.Helpers import global_preferences
from rest_framework.decorators import action
from rest_framework.response import Response
from config.helpers.Helpers import generate_fields, generate_customview_list, generate_customview
from config.helpers.Exception import exception

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project', None)
        if project_id is not None and project_id != '':
            queryset = queryset.filter(project_id=project_id)
        return queryset


    
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
                'TaskView', Task, includeactions=True)
            response.data['customview_list'] = generate_customview_list(1)
            response.data['customview'] = generate_customview(
                1, request.query_params.get('customview', None))
        except Exception as e:
            exception(e)
        return response
    
    @action(detail=False, methods=['get'])
    def forms(self, request, *args, **kwargs):
        # get form from dynamic preferences
        project_form = global_preferences['app_tasks__task_form']
        print("project_form", project_form.get('fields'))
        serializer_context = {'request': request.query_params, 'user': request.user}
        formser = LayoutSeralizers(data=project_form.get('fields'), many=True, context=serializer_context)
        formser.is_valid(raise_exception=True)
        return Response(formser.data)