from django.shortcuts import render
from django.contrib.auth.models import User

# REST Framework
from rest_framework import generics, serializers
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView



from .models import Todo, Lesson
from .serializers import TodoSerializer, LessonSerializer

from users.serializers import UserSerializer
from users.models import CustomUser as User


def home(request):
    return render(request, 'main/index.html')

# Lessons
class ListLesson(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class DetailLesson(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# To dos
class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer