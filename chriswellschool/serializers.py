from rest_framework import serializers
from .models import ContactUs, RegisterStudent


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'message', 'date_created']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterStudent
        fields = ['id', 'name', 'email', 'phone', 'date_of_birth', 'current_qualification', 'course',
                  'profile_picture', 'get_profile_picture', 'approved', 'slug', 'date_registered']
