from django.shortcuts import render, redirect
from .models import Pet, Like
from .forms import PetCreateForm
from common.models import Comment
from common.forms import CommentForm



# Create your views here.
def pet_all(request):
	pets = Pet.objects.all()

	context = {
		'pets':pets
	}
	return render(request, 'pet_list.html', context)



def pet_detail(request, pk):
	pet = Pet.objects.get(pk=pk)

	# add additional fields to 'pet' models
	pet.likes_count = pet.like_set.count()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(comment=form.cleaned_data['comment'], pet=pet)
			comment.save()

			return redirect('detail-page', pk)

	else:
		form = CommentForm()

		context = {
			'pet':pet,
			'comment_form': form,
			'comments': pet.comment_set.all(),
		}

		return render(request, 'pet_detail.html', context)



def pet_like(request, pk):
	pet = Pet.objects.get(pk=pk)
	like = Like(pet=pet,)
	like.save()
	# pet.like_set.create()
	
	# return render(request, 'pet_detail.html', context)
	return redirect('detail-page', pk)



def pet_create(request):
	if request.method == 'POST':
		# create form instance and populate it with data from the request.
		form = PetCreateForm(request.POST)
		# check if the form data is valid:
		if form.is_valid():
			# process the data and create model instance from it.
			type = form.cleaned_data['type']
			name = form.cleaned_data['name']
			age = form.cleaned_data['age']
			description = form.cleaned_data['description']
			image_url = form.cleaned_data['image_url']

			# create 'pet' model instance with the cleaned data from the form instance.
			pet = Pet(
					type=type,
					name=name,
					age=age,
					description=description,
					image_url=image_url,
				)
			# save the pet instance
			pet.save()

			return redirect('landing')
	else:
		form = PetCreateForm()
		context = {'form':form}
		return render(request, 'pet_create.html', context)

	

def pet_delete(request, pk):
	pet = Pet.objects.get(pk=pk)
	if request.method == 'POST':
		pet.delete()
		return redirect('all-page')
	else:
		context = {'pet':pet}
		return render(request, 'pet_delete.html', context)



def pet_edit(request, pk):
	pet = Pet.objects.get(pk=pk)
	if request.method == 'POST':
		# refill the form with the updated/edited form fields.
		form = PetCreateForm(request.POST)
		# check if the form data is valid.
		if form.is_valid():
			# process the data and create model instance from it.
			type = form.cleaned_data['type']
			name = form.cleaned_data['name']
			age = form.cleaned_data['age']
			description = form.cleaned_data['description']
			image_url = form.cleaned_data['image_url']

			# update the pet instance
			pet.type=type
			pet.name=name
			pet.age=age
			pet.description=description
			pet.image_url=image_url

			# save the updated pet instance to the database
			pet.save()

			# redirect to the pet-detail page
			return redirect('detail-page', pk)
	else:
		# create instance and populate it with the pet being edited's data.
		form = PetCreateForm(instance=pet)
		# put the form in a context obj (dict) to pass it to the template
		context = {
			'form': form
		}

		# render the populated form
		return render(request, 'pet_edit.html', context)

