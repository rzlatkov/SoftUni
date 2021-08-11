from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class TestChangePasswordView(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')

    def test_not_logged_in(self):
        response = self.client.get(reverse('pass-change'))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual('/accounts/login/?next=/accounts/password/change/', redirect)

    def test_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('pass-change'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_post_invalid(self):
        self.client.force_login(self.user)
        user = auth.get_user(self.client)
        old_password = user.password
        data = {
            'old_password': 'test123',
            'new_password1': 'adidas1234',
            'new_password2': 'adidas1234',
        }
        response = self.client.post(reverse('pass-change'), data)
        user = auth.get_user(self.client)
        status = response.status_code
        new_password = user.password
        self.assertEqual(old_password, new_password)
        self.assertEqual(200, status)

    def test_post_valid(self):
        self.client.force_login(self.user)
        user = auth.get_user(self.client)
        old_password = user.password
        data = {
            'old_password': 'saltking45',
            'new_password1': 'adidas1234',
            'new_password2': 'adidas1234',
        }
        response = self.client.post(reverse('pass-change'), data)
        user = auth.get_user(self.client)
        status = response.status_code
        redirect = response.headers['location']
        new_password = user.password
        self.assertNotEqual(old_password, new_password)
        self.assertEqual(302, status)
        self.assertEqual('/accounts/password/change/', redirect)