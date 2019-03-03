from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	owner = models.ForeignKey(User, default=2, on_delete=models.SET_DEFAULT)
	title = models.CharField(max_length = 150)
	description = models.TextField()

	def __str__(self):
		return self.title

class Like(models.Model):
	user = models.ManyToManyField(User)
	todo = models.OneToOneField(Todo, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id) + '-' + str(self.todo)