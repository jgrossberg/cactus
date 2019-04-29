from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Todo, Lesson

class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = (
			'id',
			'created_by',
			'created_on',
			'title',
			'content'
		)


class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo
		fields = (
			'id',
			'lesson',
			'owner',
			'added_on',
			'completed'
		)

class UserSerializer(serializers.ModelSerializer):
    # todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'staff status')#'todos')