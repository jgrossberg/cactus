from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from todos import views

urlpatterns = [

	path('', views.ListTodo.as_view()),
	 # url(r'^api/todos', views.home),
    
    path('<int:pk>/', views.DetailTodo.as_view()),


]
