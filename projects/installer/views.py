# views.py
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InstalledApp
from .utility.AppsInstall import install

# class InstallAppAPIView(APIView):

#     @extend_schema(
#         request=AppInstallSerializer,
#         summary="Install a Addons app",
#         description="This API installs the specified addons app.",
#     )
#     def post(self, request, format=None):
#         serializer = AppInstallSerializer(data=request.data)
#         if serializer.is_valid():
#             app_name = serializer.validated_data['app_name']
#             app, created = InstalledApp.objects.get_or_create(app_name=app_name)

#             if not app.is_installed:
#                 success, message = install(app_name)
#                 app.is_installed = success
#                 app.save()

#             if success:
#                 return Response({"detail": message}, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({"detail": message}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
