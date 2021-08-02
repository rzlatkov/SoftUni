from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful registration.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration.")
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('home')
