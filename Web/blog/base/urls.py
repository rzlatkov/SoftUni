from django.urls import path
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView

# django ULR resolver expects to send the req and args to a function, not a class.
# if CBV used, add as_view() which returns a function that can be called upon a request.
# as_view() creates an instance of the class, calls setup() to init attrs and then dispatch().
# dispatch() looks at the request to determine its method (GET/POST/etc) and connects it
# to a matching method or raises HttpResponseNotAllowed.
# matching methods - get(), post(), etc..

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-detail'),
    path('add-post/', AddPostView.as_view(), name='post-add'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='post-delete'),
]
