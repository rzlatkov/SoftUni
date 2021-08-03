from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm, CategoryForm
from django.urls import reverse_lazy


def category_detail_view(request, cat):
    posts_by_cat = Post.objects.filter(category__name=cat)
    context = {'posts_by_cat': posts_by_cat, 'cat': cat}
    return render(request, 'base/posts_by_category.html', context)


def category_add_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'base/add_category.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'base/categories.html'
    ordering = ('name',)


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

