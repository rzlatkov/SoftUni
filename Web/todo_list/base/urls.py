from django.urls import path
# from . import views  # custom FBV
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage  # custom CBV
from django.contrib.auth.views import LogoutView



urlpatterns = [
	path('login/', CustomLoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # next_page attr redirects us to the login page
	path('register/', RegisterPage.as_view(), name='register'),
	# path('', views.taskList, name='tasks'),  # for FBV
	path('', TaskList.as_view(), name='tasks'),  # <CBV>.as_view() is mandatory so a CBV can be used as a FBV (class => func)
	path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
	path('task-create/', TaskCreate.as_view(), name='task-create'),
	path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
	path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]

# pass - testjohn123