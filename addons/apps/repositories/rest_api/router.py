# repositories/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from addons.apps.repositories.rest_api.viewset import RepositoryViewSet

repositories_router = DefaultRouter()
repositories_router.register(r'repositories', RepositoryViewSet, basename='repository')
# repositories_router.register(r'branches', BranchViewSet, basename='branch')
# repositories_router.register(r'commits', CommitViewSet, basename='commit')

