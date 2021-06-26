from django.db import models

# Create your models here.
class Contact(models.Model):
	full_name = models.CharField(max_length=200, null=True, blank=True)
	relationship = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=254, null=True, blank=True)
	phone_number = models.CharField(max_length=50, null=True, blank=True)
	address = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.full_name