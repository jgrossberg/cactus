from django.shortcuts import render


# REST Framework
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView




from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


