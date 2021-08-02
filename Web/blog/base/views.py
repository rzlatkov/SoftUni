# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'base/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'base/home.html'
    ordering = ('date_published',)
    # context_object_name = 'posts'


class PostView(DetailView):
    model = Post
    template_name = 'base/post_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'base/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'base/edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'base/delete_post.html'

