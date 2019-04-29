from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin

from api import views

urlpatterns = [
  re_path(r'^admin/', admin.site.urls),
  re_path(r'^$', views.home, name='home'),
  re_path(r'^api-auth/', include('rest_framework.urls')),

  re_path(r'^api/', include('api.urls')),
  

  # url(r'^todos/$', views.TodosView.as_view()),
  # url(r'^todos/(?P<todo_id>[0-9]*)$', views.TodosView.as_view())

]
