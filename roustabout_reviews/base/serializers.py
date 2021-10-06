from django.contrib.auth.models import User
# from django.core.validators import validate_comma_separated_integer_list
from rest_framework import serializers
# from rest_framework_jwt.settings import api_settings as settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'url', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'password',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
