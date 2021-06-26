from django.contrib import admin
# import app's models here.
from .models import Pet

# admin user: john, pass: testjohn123, email: john@john.com

# ModelAdmin class is the representation of a model in the admin page.
class PetAdmin(admin.ModelAdmin):
	
	# customize here.
	list_display = ('name', 'type', 'age', 'description', 'likes_count', 'comments_count')
	list_filter = ('type',)

	# display more data in admin page by custom functions.
	# self is the PetAdmin instance, while obj is the Pet instance.
	def likes_count(self, obj):
		return obj.like_set.count()

	def comments_count(self, obj):
		return obj.comment_set.count()

	class Meta:
		ordering = ('type')


# register app's models by: 'admin.site.register(<model_type>)'
# admin.site.register(PetAdmin)

# to customize a model in the admin page, register both the model and its custom ModelAdmin.
admin.site.register(Pet, PetAdmin)

