from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    login_view,
    logout_view,
    ProfileView,
    UpdateProfileView,
    change_password_view,
    CustomPasswordResetView,
    CustomPasswordResetCompleteView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetDoneView,
    )

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', UpdateProfileView.as_view(), name='profile-edit'),
    path('password/change/', change_password_view, name='pass-change'),

    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# django.contrib.auth.urls package maps to:
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset'] - user submits email form
# accounts/ password_reset/done/ [name='password_reset_done'] - success message if email sent to user
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm'] - link to pass reset form in user's email
# accounts/ reset/done/ [name='password_reset_complete'] - success message if pass reset successfully
