from django.urls import path
from .views import pet_all, pet_detail, pet_like, pet_create, pet_delete, pet_edit

urlpatterns = [
	path('', pet_all, name='all-page'),
	path('details/<int:pk>/', pet_detail, name='detail-page'),
	path('like/<int:pk>/', pet_like, name='pet-like'),
	path('create/', pet_create, name='pet-create'),
	path('edit/<int:pk>', pet_edit, name='pet-edit'),
	path('delete/<int:pk>', pet_delete, name='pet-delete'),
]