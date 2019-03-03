from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from todos import views

urlpatterns = [

	path('', views.ListTodo.as_view()),

	re_path(r'^(?P<pk>[0-9])/$', views.DetailTodo.as_view()),

	re_path(r'^likes/$', views.ListLike.as_view()),
    re_path(r'^likes/(?P<pk>[0-9])/$', views.DetailLike.as_view()),

    re_path(r'^register/$', views.CreateUserView.as_view()),


]
