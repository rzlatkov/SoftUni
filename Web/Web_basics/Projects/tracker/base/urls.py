from django.urls import path
from .views import home, create_expenses, edit_expenses, delete_expenses, profile, edit_profile, delete_profile

urlpatterns = [
	path('', home, name='home-page'),
	path('create/', create_expenses, name='create-expense'),
	path('edit/<int:pk>/', edit_expenses, name='edit-expense'),
	path('delete/<int:pk>/', delete_expenses, name='delete-expense'),
	path('profile/', profile, name='profile'),
	path('profile/edit/', edit_profile, name='edit-profile'),
	path('profile/delete/', delete_profile, name='delete-profile'),
]