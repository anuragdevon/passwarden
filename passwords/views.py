from rest_framework import generics, permissions
from .models import User, Password
from .serializers import UserSerializer, PasswordSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PasswordList(generics.ListCreateAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

class PasswordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
