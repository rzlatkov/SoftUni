from django.urls import path
from .views import landing_page  # import FBVs/CBVs here one by one. Do not use '*' syntax.

urlpatterns = [
	path('', landing_page, name='landing'),
]