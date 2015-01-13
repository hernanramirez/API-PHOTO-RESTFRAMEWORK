from django.contrib.auth.models import User

from username.serializers import UserSerializer, UserProfileSerializer
from username.viewsets import CreateModelViewSet, CreateListModelViewSet

from rest_framework import permissions
from rest_framework.response import Response

class UserRegisterView(CreateModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request):
        json = []
        results = {}
        try:
            user = User.objects.get(email=str(request.GET['name']))
            results['id'] = int(user.id)
            results['email'] = user.email
            results['first_name'] = user.first_name
            results['username'] = user.username
            json.append(results)
            profileList = UserProfileSerializer(json, many=True)
            return Response(profileList.data)
        except:
            profileList = UserProfileSerializer(json, many=True)
            return Response(profileList.data)


