from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

	# a form field has a type/class.
	# widget is the representation of a form field in the HTML template.
	# Widget's type in the template is set by 'widget=form.<>'.
	# each widget has attributes by which it can be customized. (CSS, JS, etc.)
	comment = forms.CharField(required=True, widget=forms.Textarea(
		attrs={'class': 'form-control rounded-2'},),)


	class Meta:
		model = Comment
		fields = ('comment',)