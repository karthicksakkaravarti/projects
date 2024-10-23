# addons/apps/repositories/rest_api/viewset.py

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from addons.apps.repositories.models import Repository
from addons.apps.repositories.rest_api.serializers import RepositorySerializer
# Import the service
from addons.apps.repositories.services.gitea_service import GiteaService
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
import zipfile
from django.http import HttpResponse
from rest_framework import serializers
from config.helpers.forms import FormsSerializers, LayoutSeralizers
import json
from config.helpers.Helpers import generate_fields, generate_customview_list, generate_customview
from config.helpers.Exception import exception
from dynamic_preferences.registries import global_preferences_registry
from config.helpers.Helpers import global_preferences



class RepositoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing repository instances.
    """
    serializer_class = RepositorySerializer


    def get_queryset(self):
        queryset = Repository.objects.filter(owner=self.request.user)
        project_id = self.request.query_params.get('project', None)
        if project_id is not None and project_id != '':
            queryset = queryset.filter(project_id=project_id)
        return queryset


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def create(self, request, *args, **kwargs):
        """
        Create a new repository and a corresponding Gitea user and repository.
        """
        # Call the original create method to create the repository
        response_repo = super().create(request, *args, **kwargs)
        # Now create the Gitea user and repository
        import random
        import string

        def generate_random_password(length=12):
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters)
                               for i in range(length))
            return password

        user_password = generate_random_password()
        gitea_service = GiteaService()
        current_user = request.user

        # Define Gitea username and email
        gitea_email = current_user.email
        try:
            # Create Gitea User
            if not current_user.gitea_token:
                response = gitea_service.create_user(
                    username=current_user.name, password=user_password, email=gitea_email)
                print("response", response)
                user_token = gitea_service.get_user_access_token(
                    username=current_user.name, password=user_password)
                current_user.gitea_token = user_token.get('sha1')
                current_user.save()
                print("token", user_token)
            else:
                user_token = {'sha1': current_user.gitea_token}

            # Create Repository under the new user
            repo = gitea_service.create_repository(
                owner=current_user, repo_name=response_repo.data.get('name'), private=True, token=user_token.get('sha1'), description=response_repo.data.get('description'))
            print(repo)

            return Response({"message": "Repository created successfully."}, status=status.HTTP_201_CREATED)
        # if message in response, return it
        except Exception as e:
            if 'message' in e.args[0]:
                return Response({"error": e.args[0]['message']}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        """
        Fetch all details from Gitea for the specified repository.
        """
        repository = self.get_object()
        gitea_service = GiteaService()

        try:


            repo_details = gitea_service.get_repository_details(
                request.user.name, repository.name, request.user.gitea_token)
            # branches = gitea_service.get_branches(repo_owner, repo_name)
            # commits = gitea_service.get_commits(repo_owner, repo_name)

            data = {
                'repository': repo_details,
                # 'branches': branches,
                # 'commits': commits,
            }

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True, methods=['get'])
    def branches(self, request, pk=None):
        repository = self.get_object()
        gitea_service = GiteaService()
        branches = gitea_service.get_branches(request.user.name, repository.name, request.user.gitea_token)
        return Response(branches, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def commits(self, request, pk=None):
        repository = self.get_object()
        gitea_service = GiteaService()
        commits = gitea_service.get_commits(request.user.name, repository.name, request.user.gitea_token)
        return Response(commits, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def contents(self, request, pk=None):
        repository = self.get_object()
        gitea_service = GiteaService()
        contents = gitea_service.get_all_files(request.user.name, repository.name, request.query_params.get('ref', 'main'), request.user.gitea_token)
        return Response(contents, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['get'])
    def forms(self, request, *args, **kwargs):
        # get form from dynamic preferences
        project_form = global_preferences['app_repositories__repo_form']
        serializer_context = {'request': request.query_params, 'user': request.user}
        formser = LayoutSeralizers(data=project_form.get('fields'), many=True, context=serializer_context)
        formser.is_valid(raise_exception=True)
        return Response(formser.data)
    
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
                'RepositoriesView', Repository, includeactions=True)
            response.data['customview_list'] = generate_customview_list(1)
            response.data['customview'] = generate_customview(
                1, request.query_params.get('customview', None))
        except Exception as e:
            exception(e)
        return response