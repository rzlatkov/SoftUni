from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, UpdateView
from base.models import Profile
from .forms import (
    CreateUserForm,
    LoginUserForm,
    PasswordChangeFormBootstrap,
    PasswordSetFormBootstrap,
    PasswordResetFormBootstrap,
)
from base.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .decorators import logged_out_required


@logged_out_required
def register_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successful registration.")
            return redirect('home')
        else:
            for error in form.errors.as_data():
                messages.error(request, form.errors[error])
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@logged_out_required
def login_view(request):
    if request.method == "POST":
        form = LoginUserForm(request, request.POST)
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
        # else:
        #     messages.error(request, 'Invalid username or password.')
    else:
        form = LoginUserForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)


@login_required()
def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('home')


@login_required()
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeFormBootstrap(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update session hash is used to after save() so that user's session won't be invalidated.
            # if invalidated, the user will be logged out upon pass change.
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('pass-change')
        else:
            messages.error(request, 'Invalid input data.')
    else:
        form = PasswordChangeFormBootstrap(request.user)

    context = {'form': form}
    return render(request, 'registration/change_password.html', context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    # default context obj name = profile


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/edit_profile.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['username'] = self.request.user.username
        initial['email'] = self.request.user.email
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name

        return initial

    def form_valid(self, form):
        data = self.request.POST
        user = self.request.user

        user.username = data['username']
        user.email = data['email']
        user.first_name = data['first_name'].lower().capitalize()
        user.last_name = data['last_name'].lower().capitalize()
        user.save()

        self.object = form.save()
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = PasswordResetFormBootstrap


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = PasswordSetFormBootstrap


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
