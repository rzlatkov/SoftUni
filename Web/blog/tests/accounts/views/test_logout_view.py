from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class TestLogoutView(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')

    def test_not_logged_in(self):
        response = self.client.post(reverse('logout'))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual('/accounts/login/?next=/accounts/logout/', redirect)

    def test_logged_in(self):
        self.client.force_login(self.user)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        response = self.client.post(reverse('logout'))
        status = response.status_code
        self.assertEqual(302, status)
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual('/', redirect)
