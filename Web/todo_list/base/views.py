from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin  # adds user restrictions to pages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task



# Its a good practice CBVs that work with login/logout/auth/users to be in a separate app.
# LoginView is a CBV by django.
# LoginView does not use a model.
class CustomLoginView(LoginView):
	# LoginView looks for a template named 'login.html'.
	template_name = 'base/login.html'

	# by default the LoginView provides us with a form. Specify the fields in the 'fields' list.
	fields = '__all__'

	redirect_authenticated_user = True  # False by default. I.e. redirects the logged user to the homepage.

	def get_success_url(self):
		return reverse_lazy('tasks')



# FormView does not come with a built-in form as LoginView does (user login form).
# Because of that we need to specify a 'form_class'. It can be custom made or built-in form.
# UserCreationForm is a django built-in form for registration able to handle everything for us by its methods.
class RegisterPage(FormView):
	# FormView looks for a template named 'register.html'.
	template_name = 'base/register.html'
	# specify the form class/type to work with.
	form_class = UserCreationForm
	redirect_authenticated_user = True  # False by default. I.e. redirects the registered user to the login page.
	
	# send the user back to the homepage by the reverse_lazy method and the success_url attr.
	success_url = reverse_lazy('tasks')

	# form is the UserCreationForm instance that django constructed to validate the POST request.
	# to obtain data from the 'form' instance use 'cleaned_data' to remove encryption.
	# 'form_valid' method is called when valid form data has been POSTed. It returns HttpResponse to the success_url.
	# FormView constructs a UserCreationForm with request.POST and request.FILES.
	# FormView then checks form.is_valid(). If it is, the view calls 'form_valid()' with the form instance.
	def form_valid(self, form):
		# save() method saves the data to the database. It runs validation check. 
		user = form.save()
		# If not None => success.
		if user is not None:
			# login() method attaches authenticated/registered user to the current session in browser's cookies directory.
			# login() takes the current HttpRequest (self.request) obj and the User obj we want to login.
			login(self.request, user)
		# super() allows the child class to call/access the parent class's 'form_valid()' method. 
		# by returning super().form_valid(form) we basically tell the parent to validate the form instance and return the result.
		return super(RegisterPage, self).form_valid(form)

	# if request == GET and user.is_authenticated=True, restrict the register page by redirecting the logged user.
	def get(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('tasks')
		return super(RegisterPage, self).get(*args, **kwargs)



# Create your function based views here.
# def taskList(request):
# 	return HttpResponse("To Do List")

# Create your class based views here. Import from django.views.generic.<view_type>
# Inherit the django CBV to our custom CBV.
# set model=<add_developer_custom_model_here>
# CBV require templates with specific names. I.e. CBV ListView requires 'task_list.html' template.
# Template name can be overriden by setting the 'template_name' attribute.
# FBVs must be connected to templates manually. CBVs automatically connect to templates.
# Mixin is a specia type of multiple inheritance of parent classes to provide additional features.
# To change the URL to where the user will be redirected if it is not authenticated/logged in, go to settings.py and type 'LOGIN_URL = 'login' at the end.
# Add LoginRequiredMixin to each CBV you need in order to use its features.
# ListView takes care of querying the database for us and passing context data to the template.
class TaskList(LoginRequiredMixin, ListView):
	model = Task

	# override how we access the data in the templates. Default is '<model_name>_list'.
	context_object_name = 'tasks'  

	# context is a variable name -> variable value mapping (dictionary) passed to a template.
	# context processor lets you specify number of variables that get set in each context automatically.
	# we can override the context and pass user specific data to a template by the get_context_data method.
	# with get_context_data() we tell django how to manipulate/filter the queryset (list of all model instances).
	# the method then overrides the context object with the filtered data.
	def get_context_data(self, **kwargs):
		# call/inherit the base context obj from the parent class/es by super()
		context = super().get_context_data(**kwargs)
		# get all tasks for a specific (logged) user.
		context['tasks'] = context['tasks'].filter(user=self.request.user)
		# add custom data to the context
		context['count'] = context['tasks'].filter(complete=False).count()

		# on submit, get the content/user input of the text box named 'search-area'
		# add the content to a variable named 'search_input' so it can be returned/rendered back to the template.
		search_input = self.request.GET.get('search-area') or ''

		# filter the 'tasks' by the search_input var.
		if search_input:
			context['tasks'] = context['tasks'].filter(title__startswith=search_input)

		# 'search_input' is created so we can add it to the context obj and render it back.
		# This makes the 'search_input's content/input to save/stay in the text box and not disapear on each submit.
		context['search_input'] = search_input

		return context



# DetailView returns information about a simple item. Click on a task and get specific info.
# DetailView looks for a template named 'task_detail.html'
# Add LoginRequiredMixin to each CBV you need in order to use its features.
class TaskDetail(LoginRequiredMixin, DetailView):
	model = Task

	# override how we access the data in the templates. Default is 'object'. Change to 'task'.
	context_object_name = 'task'

	# override the template name. Default is '<model_name>_<CBV_type>'. Change to task.html.
	template_name = 'base/task.html'



# CreateView looks for a template named 'task_form.html'. Create it.
# Add LoginRequiredMixin to each CBV you need in order to use its features.
class TaskCreate(LoginRequiredMixin, CreateView):
	model = Task

	# By default the CreateView gives us a modelForm to work with.
	# modelForm is a class representation based on a model.
	# fields we need from our models for the form must be included in a 'fields' list.
	# fields = ['title', 'description']  # custom fields
	fields = '__all__'  # all fields from the Task model.

	fields = ['title', 'description', 'complete']
	# when form is submitted we have to redirect to a specific URL by success_url & reverse_lazy
	# send the user back to the homepage by the reverse_lazy method and the success_url attr.
	success_url = reverse_lazy('tasks')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TaskCreate, self).form_valid(form)



# UpdateView lets us update a model instance in db.
# UpdateView looks for a template named 'task_form.html'. Add link to the already created template.
# Add LoginRequiredMixin to each CBV you need in order to use its features.
class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = Task
	fields = '__all__'  # all fields from the Task model.
	success_url = reverse_lazy('tasks')



# DeleteView renders a confirmation page on delete. Then when POST request is sent, the model instance is deleted from db.
# Add LoginRequiredMixin to each CBV you need in order to use its features.
class DeleteView(LoginRequiredMixin, DeleteView):
	model = Task

	# override how we access the data in the templates. Default is 'object'. Change to 'task'.
	context_object_name = 'task'
	success_url = reverse_lazy('tasks')

	# override the template name. Default is '<model_name>_confirm_delete.html'. Create 'task_confirm_delete.html'.
	# create a form for the POST request in the 'task_confirm_delete.html' template.