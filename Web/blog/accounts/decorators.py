from django.http import HttpResponse
from django.shortcuts import redirect


def logged_out_required(view):
    """
    Does not let an authenticated user to register.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view(request, *args, **kwargs)
    return wrapper
