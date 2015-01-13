from event.models import Profile
from event.fields import HyperlinkedImageField

from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    image = HyperlinkedImageField()

    class Meta:
        model = Profile
        fields = ('user', 'title', 'image', 'address', 'latitude', 'longitude', 'upload_timestamp')