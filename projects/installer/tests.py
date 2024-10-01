# test_views.py

from rest_framework.test import APITestCase
from rest_framework import status


class InstallAppAPITest(APITestCase):

    def test_install_app(self):
        data = {'app_name': 'project'}  # Replace with an actual test app name
        response = self.client.post('/install_app/', data, format='json')  # Replace with the actual URL of your view
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
