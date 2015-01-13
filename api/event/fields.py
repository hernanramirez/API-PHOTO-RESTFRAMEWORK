from django import forms
from rest_framework.serializers import ImageField

class HyperlinkedImageField(ImageField):

    def to_native(self, value):
        request = self.context.get('request', None)
        if request and value.name:
            return request.build_absolute_uri(value.url)
        else:
            return super(HyperlinkedImageField, self).to_native(value)