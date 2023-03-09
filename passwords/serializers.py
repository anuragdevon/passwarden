from rest_framework import serializers
from .models import User, Password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Password
        fields = ('website', 'username', 'password')
