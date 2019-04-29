from rest_framework import generics

from . import models
from . import serializers

# Users
class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
	model = User
	permission_classes = [ 
		permissions.AllowAny
	]
	serializer_class = UserSerializer
