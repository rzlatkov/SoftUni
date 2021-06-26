from django import forms
from .models import Pet

class PetCreateForm(forms.ModelForm):

	CAT = 'cat'
	DOG = 'dog'
	PARROT = 'parrot'	


	PET_TYPES = [
		(CAT, 'Cat'),
		(DOG, 'Dog'),
		(PARROT, 'Parrot'),
	]

	# a form field has a type/class.
	# widget is the representation of a form field in the HTML template.
	# Widget's type in the template is set by 'widget=form.<>'.
	# each widget has attributes by which it can be customized. (CSS, JS, etc.)
	type = forms.ChoiceField(choices=PET_TYPES, required=True, widget=forms.Select(
		attrs={'class': 'form-control'},),)

	name = forms.CharField(required=True, widget=forms.TextInput(
		attrs={'class': 'form-control'},),)

	age = forms.IntegerField(required=True, widget=forms.TextInput(
		attrs={'class': 'form-control', 'type': 'number'},),)

	image_url = forms.URLField(required=True, widget=forms.TextInput(
		attrs={'class': 'form-control'},),)

	description = forms.CharField(required=True, widget=forms.Textarea(
		attrs={'class': 'form-control rounded-2'},),)


	class Meta:
		model = Pet
		fields = '__all__'