from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from api import views

urlpatterns = [

	path('', views.ListLesson.as_view()),

	re_path(r'^lessons/$', views.ListLesson.as_view()),
    re_path(r'^lessons/(?P<pk>[0-9])/$', views.DetailLesson.as_view()),
	
	re_path(r'^todos/$', views.ListTodo.as_view()),
    re_path(r'^todos/(?P<pk>[0-9])/$', views.DetailTodo.as_view()),

	re_path(r'^users/$', views.ListUser.as_view()),
	re_path(r'^users/(?P<pk>[0-9])/$', views.DetailUser.as_view()),


    # re_path(r'^register/$', views.CreateUserView.as_view()),

]
