from django.contrib.auth.models import User

from event.models import Profile
from event.serializers import ProfileSerializer
from event.viewsets import CreateModelViewSet, CreateListModelViewSet

from rest_framework import permissions
from rest_framework.response import Response

class EventUploadListView(CreateListModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def pre_save(self, obj):
        print 'oooooo'
        obj.user = self.request.user

    def post(self, request, *args, **kwargs):
        request.DATA['user_id'] = self.request.user.id
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)