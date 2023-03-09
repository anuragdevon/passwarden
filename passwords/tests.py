from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import Password
from .serializers import PasswordSerializer

User = get_user_model()

class PasswordTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.password = Password.objects.create(user=self.user, website='example.com', username='testuser', password='password')

    def test_password_list(self):
        url = '/passwords/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_password_detail(self):
        url = '/passwords/{}/'.format(self.password.id)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        serializer = PasswordSerializer(instance=self.password)
        self.assertEqual(response.data, serializer.data)

    def test_password_create(self):
        url = '/passwords/'
        data = {'website': 'example2.com', 'username': 'testuser2', 'password': 'password2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Password.objects.count(), 2)

    def test_password_update(self):
        url = '/passwords/{}/'.format(self.password.id)
        data = {'website': 'example_updated.com', 'username': 'testuser_updated', 'password': 'password_updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.password.refresh_from_db()
        self.assertEqual(self.password.website, 'example_updated.com')
        self.assertEqual(self.password.username, 'testuser_updated')
        self.assertEqual(self.password.password, 'password_updated')

    def test_password_delete(self):
        url = '/passwords/{}/'.format(self.password.id)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Password.objects.count(), 0)
