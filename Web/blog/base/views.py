from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import (PostForm,
                    CategoryForm,
                    CommentForm,
                    )
from django.urls import reverse_lazy
from django.db.models import Q


def post_like_view(request, pk):
    # pk == post.id
    post = get_object_or_404(Post, pk=pk)
    # check if post has been already liked from the user
    if post.likes.filter(id=request.user.id).exists():
        # unlike
        post.likes.remove(request.user)
    else:
        # add user validation here
        # like
        post.likes.add(request.user)

    return redirect('post-detail', pk)


def comment_add_view(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = Post.objects.get(pk=pk)
            new_comment.save()
            return redirect('post-detail', pk)
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'base/add_comment.html', context)


def category_detail_view(request, cat):
    cat = cat.capitalize().replace('-', ' ')
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

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            result = self.model.objects.filter(Q(name__icontains=query))
        else:
            result = self.model.objects.all()
        return result


class HomeView(ListView):
    model = Post
    template_name = 'base/home.html'
    ordering = ('date_published',)
    # default context obj name = objects_list
    # context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            result = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(category__name__icontains=query) |
                Q(author__username__icontains=query)
            )
        else:
            result = self.model.objects.all()
        return result


class PostView(DetailView):
    model = Post
    template_name = 'base/post_details.html'
    # context obj name defaults to the lowercased version of the model name

    # inherit get_context_data() from superclass and extend it:
    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        # call base implementation to get context data
        context = super().get_context_data(**kwargs)

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # add variable to context data
        context['likes'] = post.likes_count()
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'base/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'base/edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'base/delete_post.html'

