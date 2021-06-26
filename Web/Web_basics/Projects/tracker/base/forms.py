from django import forms
from .models import Profile, Expense

class RegisterForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['budget', 'first_name', 'last_name',]

class CreateExpense(forms.ModelForm):
	
	class Meta:
		model = Expense
		fields = ['title','description','image_url', 'price']

		labels = {
			'image_url': 'Link to Image'
		}