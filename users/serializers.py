from rest_framework import serializers
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=500)
	password = serializers.CharField(max_length=500, write_only=True)