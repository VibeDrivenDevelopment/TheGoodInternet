from user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'display_name', 'email', 'phone_number', 'profile_picture']