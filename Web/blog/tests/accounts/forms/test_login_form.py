from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import LoginUserForm


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
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = LoginUserForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_empty_username_field(self):
        data = {
            'password': 'saltking45'
        }
        form = LoginUserForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_empty_password_field(self):
        data = {
            'username': 'john',
        }
        form = LoginUserForm(data=data)
        print(form.errors)
        self.assertEqual(form.errors['password'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def test_invalid_username_credential(self):
        data = {
            'username': 'rocky',
            'password': 'saltking45',
        }
        form = LoginUserForm(data=data)
        print(form.errors)
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertEqual(form.non_field_errors()[0], message)
        self.assertFalse(form.is_valid())

    def test_invalid_password_credential(self):
        data = {
            'username': 'john',
            'password': 'wtfafa345',
        }
        form = LoginUserForm(data=data)
        print(form.errors)
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
        print(form.errors)
        message = 'Please enter a correct username and password. Note that both fields may be case-sensitive.'
        self.assertEqual(form.non_field_errors()[0], message)
        self.assertFalse(form.is_valid())