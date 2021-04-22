from rest_framework import serializers
from user.models import UserDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            'user_name',
            'user_email',
            'user_password',
            'user_mobileNo'
        )
        