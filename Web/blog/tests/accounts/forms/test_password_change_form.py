from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.forms import PasswordChangeFormBootstrap


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
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = PasswordChangeFormBootstrap(data=data, user=self.user)
        print(form.errors)
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
        print(form.errors)
        self.assertEqual(form.errors['old_password'], ['Your old password was entered incorrectly. Please enter it again.'])
        self.assertFalse(form.is_valid())

    def test_different_newPasswords(self):
        data = {
            'old_password': 'saltking45',
            'new_password1': 'adidas1234',
            'new_password2': 'adidas12345',
        }
        form = PasswordChangeFormBootstrap(data=data, user=self.user)
        print(form.errors)
        self.assertEqual(form.errors['new_password2'], ['The two password fields didn’t match.'])
        self.assertFalse(form.is_valid())