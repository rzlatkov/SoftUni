from django.db import models

# Create your models here.
class Pet(models.Model):

	# field choices is a list of tuples to use as choices for a given field.
	# if choices are given, they're enforced by model validation.
	# the form widget will become a select box with the choices instead of the standard text-field.
	# the first element in each tuple is the actual value to be set on the model.
	# the second element in each tuple is the human-readable name.
	# add reference to the first element in each tuple before adding to the list of choices.
	# access by reference example: Pet.CAT
	CAT = 'cat'
	DOG = 'dog'
	PARROT = 'parrot'	


	PET_TYPES = [
		(CAT, 'Cat'),
		(DOG, 'Dog'),
		(PARROT, 'Parrot'),
	]

	# place null=true and blank=true during development ONLY, for easier migrations.
	# max_length is a required attribute for a CharField class and its subclasses.
	type = models.CharField(max_length=50, choices=PET_TYPES, null=True, blank=True)
	name = models.CharField(max_length=50)
	age = models.PositiveIntegerField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	# copy-paste image URL from google images.
	image_url = models.URLField(max_length=200, null=True, blank=True)

	# define how model instances will be shown in the admin page.
	def __str__(self):
		return self.name

class Like(models.Model):

	# create One-to-Many relationship by models.ForeignKey(<relation_model_type>,<on_delete=...>)
	# a 'like' instance can point to a single 'pet' instance.
	# a 'pet' instance can have/point to many 'like' instance.
	# add the 'ForeignKey' here, because a 'like' points to a single 'pet'.
	# the model where the foreignkey field is added can access its relation by i.e.: Like.pet
	# the other model can reverse access its relation by i.e.: Pet.like_set.
	# on_delete tells django what to do when a relation is deleted from the database.
	# .CASCADE tells django that if a 'Pet' instance is deleted, its 'like' instances should be also deleted.
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)