from rest_framework import serializers

from .models import User, Ident

class UserSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=255)
    lastName = serializers.CharField(max_length=255)
    photo = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class IdentSerializer(serializers.Serializer):
    photo = serializers.CharField()

    def create(self, validated_data):
        return Ident.objects.create(**validated_data)