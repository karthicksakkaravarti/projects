# project_management_repo/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from addons.apps.documents.rest_api.viewset import DocumentViewSet, CategoryViewSet


documents_router = routers.DefaultRouter()
documents_router.register(r'documents', DocumentViewSet)
documents_router.register(r'categories', CategoryViewSet)
