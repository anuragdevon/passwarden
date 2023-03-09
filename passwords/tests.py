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

