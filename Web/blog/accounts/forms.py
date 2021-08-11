from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.models import User
from .mixins import BootstrapifyFormMixin


class CreateUserForm(BootstrapifyFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginUserForm(BootstrapifyFormMixin, AuthenticationForm):
    class Meta:
        model = User


class PasswordChangeFormBootstrap(BootstrapifyFormMixin, PasswordChangeForm):
    pass


class PasswordResetFormBootstrap(BootstrapifyFormMixin, PasswordResetForm):
    pass


class PasswordSetFormBootstrap(BootstrapifyFormMixin, SetPasswordForm):
    pass
