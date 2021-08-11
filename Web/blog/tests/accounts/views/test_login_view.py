from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User


class TestLoginView(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')

    def test_not_logged_out(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('login'))
        status = response.status_code
        redirect = response.headers['location']  # 'home'
        self.assertEqual(302, status)
        self.assertEqual('/', redirect)

    def test_get(self):
        response = self.client.get(reverse('login'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_post_invalid(self):
        data = {
            'username': 'jo',
            'password': 'tes231456',
        }
        response = self.client.post(reverse('login'), data)
        status = response.status_code

        self.assertEqual(200, status)
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)

    def test_post_valid(self):
        data = {
            'username': 'john',
            'password': 'saltking45',
        }
        response = self.client.post(reverse('login'), data)
        status = response.status_code
        redirect = response.headers['location']  # 'home'
        self.assertEqual(302, status)
        self.assertEqual('/', redirect)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertEqual('john', user.username)
