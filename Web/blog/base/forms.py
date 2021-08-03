from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()