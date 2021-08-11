from django.test import TestCase
from accounts.forms import CreateUserForm


class TestRegisterForm(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'john',
            'email': 'john@john.com',
            'password1': 'saltking45',
            'password2': 'saltking45',
        }
        form = CreateUserForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = CreateUserForm(data=data)
        print(form.errors)
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
        print(form.errors)
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
        print(form.errors)
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
        print(form.errors)
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
        print(form.errors)
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
        print(form.errors)
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
        print(form.errors)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertFalse(form.is_valid())