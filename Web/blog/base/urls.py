from django.urls import path
from .views import (
    HomeView,
    PostView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    CategoryListView,
    category_detail_view,
    category_add_view,
    comment_add_view,
    post_like_view,
    )


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-detail'),
    path('post/add/', AddPostView.as_view(), name='post-add'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='post-delete'),
    path('post/like/<int:pk>', post_like_view, name='post-like'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/<str:cat>', category_detail_view, name='category-detail'),
    path('category/add/', category_add_view, name='category-add'),
    path('comment/add/<int:pk>', comment_add_view, name='comment-add'),
    # path('comment/edit/<int:pk>', , name='comment-edit'),
    # path('comment/delete/<int:pk>', , name='comment-delete'),
]
