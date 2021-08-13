from django import forms
from .models import Post, Category, Comment, Profile
from accounts.mixins import BootstrapifyFormMixin
from .validators import first_last_name_len, letters_n_whitespaces, alphanumeric


class PostForm(BootstrapifyFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'snippet']


class CategoryForm(BootstrapifyFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

    # def clean_name(self):
    #     return self.cleaned_data['name'].lower().capitalize()


class CommentForm(BootstrapifyFormMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content',)


class ProfileForm(BootstrapifyFormMixin, forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               validators=[alphanumeric])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 validators=[first_last_name_len, letters_n_whitespaces])
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                validators=[first_last_name_len, letters_n_whitespaces])

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
