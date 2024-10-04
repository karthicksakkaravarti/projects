from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import TodoItem
from projects.setup.users.models import User
from django.contrib.auth import get_user_model
from unittest.mock import patch


class TodoItemViewSetTestCase(TestCase):
    # def setUp(self):
    #     # Create some initial data for testing
    #     self.client = APIClient()
    #     self.todo_item_data = {'title': 'Test Todo Item', 'completed': False}
    #     self.todo_item = TodoItem.objects.create(**self.todo_item_data)

    def setUp(self):
        self.client = APIClient()

        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )

        # Log in the user using Django Allauth
        self.client.login(email='testuser@example.com', password='testpassword')

        # Configure the client to include the token in requests
        # self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create a test TodoItem if needed
        self.todo_item_data = {'title': 'Test Todo Item', 'completed': False}
        self.todo_item = TodoItem.objects.create(**self.todo_item_data)
        self.url = '/addons/apps/todo/api/todos/'  # Update this URL as per your API configuration

    def test_list_todo_items(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_todo_item(self):
        response = self.client.get(f'{self.url}{self.todo_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo_item_data['title'])
        self.assertEqual(response.data['completed'], self.todo_item_data['completed'])

    def test_create_todo_item(self):
        response = self.client.post(self.url, self.todo_item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TodoItem.objects.count(), 2)  # Assuming there's already one item in the database

    def test_update_todo_item(self):
        updated_data = {'title': 'Updated Todo Item', 'completed': True}
        response = self.client.put(f'{self.url}{self.todo_item.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo_item.refresh_from_db()
        self.assertEqual(self.todo_item.title, updated_data['title'])
        self.assertEqual(self.todo_item.completed, updated_data['completed'])

    def test_delete_todo_item(self):
        response = self.client.delete(f'{self.url}{self.todo_item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TodoItem.objects.count(), 0)  # Assuming there's only one item to begin with
