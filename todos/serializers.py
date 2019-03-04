from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Todo, Like


class TodoSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Todo
		
		fields = (
				'id',
			'owner',
			'title',
			'description',
		)

class LikeSerializer(serializers.ModelSerializer):

	class Meta:

		"""Serialize the Todo into existence"""
		todo = TodoSerializer()

		fields = (
			'id',
			'user',
			'todo',
		)
		model = Like

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'todos')