from django.contrib.auth.models import User

from username.fields import PasswordField

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class UserProfileSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance._id = attrs.get('id', instance._id)  
            instance.email = attrs.get('email', instance.email)
            instance.first_name = attrs.get('first_name', instance.first_name)
            instance.username = attrs.get('username', instance.username)          
            return instance

        return Username(attrs.get('id'))


