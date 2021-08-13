from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import (PostForm,
                    CategoryForm,
                    CommentForm,)
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator


@login_required()
def post_like_view(request, pk):
    # pk == post.id
    post = get_object_or_404(Post, pk=pk)
    # check if post has been already liked from the user
    if post.likes.filter(id=request.user.id).exists():
        # unlike
        post.likes.remove(request.user)
    else:
        # like
        post.likes.add(request.user)

    return redirect('post-detail', pk)


@login_required()
def comment_add_view(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = get_object_or_404(Post, pk=pk)
            # new_comment.post = Post.objects.get(pk=pk)
            new_comment.save()
            return redirect('post-detail', pk)
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'base/add_comment.html', context)


@login_required()
def comment_edit_view(request, pk):
    # comment = Comment.objects.get(pk=pk)
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.name = form.cleaned_data['name']
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('post-detail', comment.post.pk)
    else:
        if comment.author.pk != request.user.pk:
            return HttpResponseForbidden('You cannot edit/delete other users content.')
        form = CommentForm(instance=comment)

    context = {'form': form}
    return render(request, 'base/edit_comment.html', context)


@login_required()
def comment_delete_view(request, pk):
    # comment = Comment.objects.get(pk=pk)
    comment = get_object_or_404(Comment, pk=pk)
    # post = Post.objects.get(comments__pk=pk)
    post = get_object_or_404(Post, comments__pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('post-detail', post.pk)
    else:
        if comment.author.pk != request.user.pk:
            return HttpResponseForbidden('You cannot edit/delete other users content.')
    context = {'comment': comment}
    return render(request, 'base/delete_comment.html', context)


def category_detail_view(request, cat):
    cat = cat.capitalize().replace('-', ' ')
    qs = get_object_or_404(Category, name=cat)
    posts_by_cat = Post.objects.filter(category__name=cat)

    paginator = Paginator(posts_by_cat, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts_by_cat': posts, 'cat': cat}
    return render(request, 'base/posts_by_category.html', context)


@login_required()
@staff_member_required()
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
    paginate_by = 2

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
    paginate_by = 2

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

    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # add variable to context data
        context['likes'] = post.likes_count()
        context['liked'] = liked
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'base/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'base/edit_post.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author.pk != self.request.user.pk:
            return HttpResponseForbidden('You cannot edit/delete other users content.')
        return super().post(request, *args, **kwargs)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'base/delete_post.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author.pk != self.request.user.pk:
            return HttpResponseForbidden('You cannot edit/delete other users content.')
        return super().post(request, *args, **kwargs)

