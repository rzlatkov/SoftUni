from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Post, Category, Comment, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'snippet']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        return self.cleaned_data['name'].lower().capitalize()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'profile_picture',
                  'location',
                  'birth_date',
                  'bio',
                  'facebook_url',
                  'twitter_url',
                  'github_url',
                  'instagram_url',
                  'linkedin_url',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
        self.fields['facebook_url'].widget.attrs['class'] = 'form-control'
        self.fields['twitter_url'].widget.attrs['class'] = 'form-control'
        self.fields['github_url'].widget.attrs['class'] = 'form-control'
        self.fields['instagram_url'].widget.attrs['class'] = 'form-control'
        self.fields['linkedin_url'].widget.attrs['class'] = 'form-control'
