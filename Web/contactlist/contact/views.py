from django.shortcuts import render, redirect
from .models import Contact
from django.core.validators import validate_email

# Create your views here.
def index(request):
	# query the model instances from the database.
	contacts = Contact.objects.all()
	
	search_input = request.GET.get('search-area')
	if search_input:
		contacts = Contact.objects.filter(full_name__icontains=search_input)
	else:
		contacts = Contact.objects.all()
		search_input = ''
	# pass the context dict obj to the template
	context = {'contacts':contacts, 'search_input':search_input}
	return render(request, 'contact/index.html', context)

def addContact(request):
	# on submit, a POST request is made. It is a dictionary obj containig the form fields.
	# Access a form field from the template by its key/name in the POST dictionary obj.
	if request.method == 'POST':
		new_contact = Contact(
				full_name=request.POST['fullname'],
				relationship=request.POST['relationship'],
				email=request.POST['email'],
				phone_number=request.POST['phone-number'],
				address=request.POST['address'],
			)
		new_contact.save()
		return redirect('index')
	return render(request, 'contact/new.html')

# passed arguments from the URL pattern should be named the same when passed to the view function.
def contactProfile(request, pk):
	user = Contact.objects.get(id=pk)
	return render(request, 'contact/contact-profile.html', {'contact': user})

def editContact(request, pk):
	user = Contact.objects.get(id=pk)
	if request.method == 'POST':
		user.full_name = request.POST['fullname']
		user.relationship = request.POST['relationship']
		user.email = request.POST['email']
		user.phone_number = request.POST['phone-number']
		user.address = request.POST['address']

		user.save()

		# to pass arguments from a view to an URL pattern, the name/key of the argument in redirect() 
		# should be the same with the one in the URL. The variable/agrument type should be compatible with the path converter.
		# path converters: str, int, slug, uuid, path
		return redirect('profile', pk=str(user.id))
	return render(request, 'contact/edit.html', {'contact':user})

def deleteContact(request, pk):
	user = Contact.objects.get(id=pk)
	if request.method == 'POST':
		user.delete()
		return redirect('index')
	return render(request, 'contact/delete.html', {'contact':user})