from django.shortcuts import render
from django.contrib.auth.models import User

# REST Framework
from rest_framework import generics, serializers
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



from .models import Todo, Like
from .serializers import TodoSerializer, LikeSerializer


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListLike(generics.ListCreateAPIView):
	queryset = Like.objects.all()
	serializer_class = LikeSerializer

class DetailLike(generics.RetrieveUpdateDestroyAPIView):
	queryset = Like.objects.all()
	serializer_class = LikeSerializer	

class CreateUserView(generics.CreateAPIView):
	model = User
	permission_classes = [ 
		permissions.AllowAny
	]
	serializer_class = serializers.ModelSerializer