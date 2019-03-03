# todos/serializers.py
from rest_framework import serializers
from .models import Todo, Like


class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'owner',
			'title',
			'description',
		)
		model = Todo

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