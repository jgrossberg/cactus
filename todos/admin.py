from django.contrib import admin

from .models import Todo, Like

admin.site.register(Todo)
admin.site.register(Like)