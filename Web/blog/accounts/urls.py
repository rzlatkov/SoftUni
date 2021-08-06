from django.urls import path
from .views import (
    register_view,
    login_view,
    logout_view,
    ProfileView,
    UpdateProfileView,
    change_password_view,
    )

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', UpdateProfileView.as_view(), name='profile-edit'),
    path('password/change/', change_password_view, name='pass-change'),
]
