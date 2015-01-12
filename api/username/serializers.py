from username.models import Photo
from username.fields import PasswordField, HyperlinkedImageField
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class PhotoSerializer(serializers.ModelSerializer):
    image = HyperlinkedImageField()
    #user = serializers.Field()

    class Meta:
        model = Photo
        fields = ('title', 'user','image','upload_timestamp')