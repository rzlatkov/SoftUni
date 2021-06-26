from django.contrib import admin
from .models import Task

# Register your models here, so they can pop up in admin page and be manipulated.
admin.site.register(Task)