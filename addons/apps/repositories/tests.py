# repositories/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from addons.apps.repositories.models import Repository

class RepositoryAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token_url = reverse('token_obtain_pair')
        self.repo_url = reverse('repository-list')
        # Obtain JWT token
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    
    def test_create_repository(self):
        data = {'name': 'testrepo', 'description': 'A test repository'}
        response = self.client.post(self.repo_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Repository.objects.count(), 1)
        self.assertEqual(Repository.objects.get().name, 'testrepo')
    
    def test_list_repositories(self):
        Repository.objects.create(name='repo1', owner=self.user)
        Repository.objects.create(name='repo2', owner=self.user)
        response = self.client.get(self.repo_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
