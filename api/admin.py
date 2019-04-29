from django.contrib import admin

from .models import Todo, Lesson

admin.site.register(Todo)
admin.site.register(Lesson)