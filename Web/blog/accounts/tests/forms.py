from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import CreateUserForm, LoginUserForm, PasswordChangeFormBootstrap


class TestRegisterForm(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': 'saltking45',
            'password2': 'saltking45',
        }
        form = CreateUserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_common_password(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': 'test1234',
            'password2': 'test1234',
        }
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['password2'], ['This password is too common.'])
        self.assertFalse(form.is_valid())

    def test_password_similar_to_email(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': 'john@john.com',
            'password2': 'john@john.com',
        }
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['password2'], ['The password is too similar to the email address.'])
        self.assertFalse(form.is_valid())

    def test_short_password(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': 'as',
            'password2': 'as',
        }
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['password2'], ['This password is too short. It must contain at least 8 characters.'])
        self.assertFalse(form.is_valid())

    def test_only_digits_password(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': '123456789555',
            'password2': '123456789555',
        }
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['password2'], ['This password is entirely numeric.'])
        self.assertFalse(form.is_valid())

    def test_different_passwords(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': 'saltking45',
            'password2': 'saltking69',
        }
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        data = {
            'username': 'john',
            'email': 'johnjohn.om',
            'password1': 'saltking45',
            'password2': 'saltking45',
        }
        form = CreateUserForm(data=data)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertFalse(form.is_valid())


class TestLoginForm(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')

    def test_valid_form(self):
        data = {
            'username': 'john',
            'password': 'saltking45',
        }
        form = LoginUserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = LoginUserForm(data=data)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_empty_username_field(self):
        data = {
            'password': 'saltking45'
        }
        form = LoginUserForm(data=data)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_empty_password_field(self):
        data = {
            'username': 'john',
        }
        form = LoginUserForm(data=data)
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_invalid_username_credential(self):
        data = {
            'username': 'rocky',
            'password': 'saltking45',
        }
        form = LoginUserForm(data=data)
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertEqual(form.non_field_errors()[0], message)
        self.assertFalse(form.is_valid())

    def test_invalid_password_credential(self):
        data = {
            'username': 'john',
            'password': 'wtfafa345',
        }
        form = LoginUserForm(data=data)
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertEqual(form.non_field_errors()[0], message)
        self.assertFalse(form.is_valid())

    def test_inActive_account(self):
        self.user.is_active = False
        self.user.save()
        data = {
            'username': 'john',
            'password': 'saltking45',
        }
        form = LoginUserForm(data=data)
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertEqual(form.non_field_errors()[0], message)
        self.assertFalse(form.is_valid())


class TestPasswordChangeForm(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')

    def test_valid_form(self):
        data = {
            'old_password': 'saltking45',
            'new_password1': 'adidas1234',
            'new_password2': 'adidas1234',
        }
        form = PasswordChangeFormBootstrap(data=data, user=self.user)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = PasswordChangeFormBootstrap(data=data, user=self.user)
        self.assertEqual(form.errors['old_password'], ['This field is required.'])
        self.assertEqual(form.errors['new_password1'], ['This field is required.'])
        self.assertEqual(form.errors['new_password2'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_invalid_oldPassword(self):
        data = {
            'old_password': 'ugabuga23',
            'new_password1': 'adidas1234',
            'new_password2': 'adidas1234',
        }
        form = PasswordChangeFormBootstrap(data=data, user=self.user)
        self.assertEqual(form.errors['old_password'], ['Your old password was entered incorrectly. Please enter it again.'])
        self.assertFalse(form.is_valid())

    def test_different_newPasswords(self):
        data = {
            'old_password': 'saltking45',
            'new_password1': 'adidas1234',
            'new_password2': 'adidas12345',
        }
        form = PasswordChangeFormBootstrap(data=data, user=self.user)
        self.assertEqual(form.errors['new_password2'], ['The two password fields didn’t match.'])
        self.assertFalse(form.is_valid())