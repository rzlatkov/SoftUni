from django.contrib import admin
# import app's models here.
from .models import Comment

# admin user: john, pass: testjohn123, email: john@john.com


# register app's models by: 'admin.site.register(<model_type>)'
admin.site.register(Comment)
