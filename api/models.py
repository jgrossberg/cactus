from django.db import models

from users.models import CustomUser


class Lesson(models.Model):
	created_by = models.ForeignKey(CustomUser, 
		related_name='owner',
		on_delete=models.CASCADE,
		default=1
	)
	created_on = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length = 150)
	content = models.TextField()

	def __str__(self):
		return self.title

class Todo(models.Model):
	owner = models.ForeignKey(CustomUser,
		on_delete=models.CASCADE,
		default = 1
	)
	lesson = models.ForeignKey(Lesson,
		on_delete=models.CASCADE,
		null=True
	)
	added_on = models.DateTimeField(auto_now=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.id

