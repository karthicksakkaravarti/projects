# docs/views.py

from rest_framework import viewsets, permissions
from addons.apps.documents.models import Document, Category
from addons.apps.documents.rest_api.serializers import DocumentSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from config.helpers.forms import FormsSerializers, LayoutSeralizers
from config.helpers.Helpers import global_preferences


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset

    def perform_create(self, serializer):
        # Get or create category
        print("serializer", serializer.validated_data)
        category, created = Category.objects.get_or_create(name=serializer.validated_data['category'])
        serializer.save(category=category, created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def forms(self, request, *args, **kwargs):
        # get form from dynamic preferences
        project_form = global_preferences['app_documents__document_form']
        print("project_form", project_form.get('fields'))
        serializer_context = {'request': request.query_params, 'user': request.user}
        formser = LayoutSeralizers(data=project_form.get('fields'), many=True, context=serializer_context)
        formser.is_valid(raise_exception=True)
        return Response(formser.data)
