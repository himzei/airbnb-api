from rest_framework import serializers 
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        exclude = ("groups", "user_permissions", "password", "last_login", "is_superuser", "is_active", "is_staff", "date_joined", "favs")