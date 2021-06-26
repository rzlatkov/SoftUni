from django.shortcuts import render, redirect
from .models import Profile, Expense
from .forms import RegisterForm, CreateExpense




# view updated and done!

def home(request):
	if Profile.objects.first():
		expenses = Expense.objects.all()
		profile = Profile.objects.first()

		# sum_expenses = sum(Expense.objects.values_list('price', flat=True))
		sum_expenses = sum(e.price for e in expenses)

		profile.budget_left = profile.budget - sum_expenses

		context = {
			'expenses': expenses,
			'profile': profile,
		}
		return render(request, 'home-with-profile.html', context)
	else:
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():

				form.save()
				
				# profile = Profile(
				# 		first_name=form.cleaned_data['first_name'],
				# 		last_name=form.cleaned_data['last_name'],
				# 		budget=form.cleaned_data['budget'],
				# 	)
				# profile.save()

				return redirect('home-page')
		else:
			form = RegisterForm()

			context = {
				'form': form,
			}
			return render(request, 'home-no-profile.html', context)




# view updated and done!

def create_expenses(request):
	if request.method == 'POST':
		form = CreateExpense(request.POST)
		if form.is_valid():

			form.save()

			# expense = Expense(
			# 		title=form.cleaned_data['title'],
			# 		image_url=form.cleaned_data['image_url'],
			# 		description=form.cleaned_data['description'],
			# 		price=form.cleaned_data['price'],
			# 	)
			# expense.save()

			return redirect('home-page')
		return redirect('create-expense')
	else:
		form = CreateExpense()

		context = {
				'form': form,
			}
		return render(request, 'expense-create.html', context)




# view updated and done!

def edit_expenses(request, pk):
	expense = Expense.objects.get(pk=pk)

	if request.method == 'POST':
		form = CreateExpense(request.POST, instance=expense)
		if form.is_valid():

			# expense.title = form.cleaned_data['title']
			# expense.image_url = form.cleaned_data['image_url']
			# expense.description = form.cleaned_data['description']
			# expense.price = form.cleaned_data['price']

			# expense.save()

			form.save()

			return redirect('home-page')
	else:
		form = CreateExpense(instance=expense)
		
		context = {
			'form': form,
		}
		return render(request,'expense-edit.html',context)




# view updated and done!

def delete_expenses(request, pk):
	expense = Expense.objects.get(pk=pk)

	if request.method == 'POST':
		expense.delete()
		return redirect('home-page')
	else:
		form = CreateExpense(instance=expense)

		form.fields['title'].widget.attrs['readonly'] = True
		form.fields['description'].widget.attrs['readonly'] = True
		form.fields['image_url'].widget.attrs['readonly'] = True
		form.fields['price'].widget.attrs['readonly'] = True

		context = {
			'form': form,
		}

		return render(request,'expense-delete.html',context)




# view updated and done!

def profile(request):
	expenses = Expense.objects.all()
	profile = Profile.objects.first()

	# sum_expenses = sum(Expense.objects.values_list('price', flat=True))
	sum_expenses = sum(e.price for e in expenses)

	profile.budget_left = profile.budget - sum_expenses

	context = {
		'profile': profile,
	}

	return render(request, 'profile.html', context)




# view updated and done!

def edit_profile(request):
	profile = Profile.objects.first()

	if request.method == 'POST':
		# populate the form with the POST request data and update the profile instance (2nd argument)
		form = RegisterForm(request.POST, instance=profile)
		if form.is_valid():
			# profile.first_name = form.cleaned_data['first_name']
			# profile.last_name = form.cleaned_data['last_name']
			# profile.budget = form.cleaned_data['budget']
			# profile.save()


			# the save() method creates and saves a db obj from the data bound to the form.
			# a custom modelform can accept an existing model instance as the kwarg 'instance='.
			# if 'instance' is supplied the save() will update that model instance.
			# if not supplied, the save() will create a new model instance
			form.save()

			return redirect('profile')
	else:

		# the 1st kwarg of when instantiating a form is the data we want to pass.
		# in this case we pass a model instance to fill the form.
		form = RegisterForm(instance=profile)

		context = {
			'form':form,
		}
		return render(request, 'profile-edit.html', context)




# view updated and done!

def delete_profile(request):
	if request.method == 'POST':

		Profile.objects.all().delete()
		Expense.objects.all().delete()

		return redirect('home-page')
	else:
		return render(request, 'profile-delete.html')