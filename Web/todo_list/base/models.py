from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	# null=True means the value can be empty in db without errors. Do this during dev to makemigrations easier.
	# blank=True means the value can be empty in a FORM without errors.
	# auto_now_add=True means take the date and time on creation and do not update it in the future.
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # import django User model and make One2Many relation
	title = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)	
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True) # get date and time when created.

	# representation of the obj instance
	def __str__(self):
		return self.title

	# class Meta adds functionality similar to a decorator.
	class Meta:
		# order by complete status when requesting a QuerySet
		ordering = ['complete']