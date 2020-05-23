from .models import RDUser
from rest_framework import serializers
from django.utils import timezone

class RDUserSerializer(serializers.Serializer):
    is_taxpayer = serializers.BooleanField(default=True)
    is_taxcollector = serializers.BooleanField(default=False)
    is_auditor = serializers.BooleanField(default=False)
    is_systemAdmin = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=False)
    email = serializers.EmailField( required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    DOB = serializers.DateField(default=timezone.now().date())
    password = serializers.CharField(
        write_only=True,
        required=True
    )

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return RDUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)