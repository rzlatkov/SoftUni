from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core import mail


class ProfileDetailsTest(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='test123', email='john@john.com')

    def test_get_when_logged_should_getProfileData(self):
        self.client.force_login(self.user)
        self.user.profile.bio = 'asd'
        self.user.profile.location = 'sofia'
        self.user.profile.profile_picture = 'path/jordan.jpg'
        self.user.save()

        response = self.client.get(reverse('profile', kwargs={'pk': self.user.pk}))

        self.assertEqual(self.user.id, response.context['profile'].user.id)
        self.assertEqual('asd', response.context['profile'].bio)
        self.assertEqual('sofia', response.context['profile'].location)
        self.assertEqual('path/jordan.jpg', response.context['profile'].profile_picture)
        self.assertEqual('john@john.com', response.context['profile'].user.email)

    def test_get_when_logged_should_getNoProfileData(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile', kwargs={'pk': self.user.pk}))

        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertIsNone(response.context['profile'].birth_date)
        self.assertIsNone(response.context['profile'].facebook_url)
        self.assertEqual('', response.context['profile'].bio)
        self.assertEqual('', response.context['profile'].profile_picture)


class TestRegisterView(TestCase):
    def setUp(self) -> None:
        # client = browser
        self.client = Client()

    def test_not_logged_out(self):
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.client.force_login(self.user)
        response = self.client.get(reverse('register'))
        status = response.status_code
        redirect = response.headers['location']  # 'home'
        self.assertEqual(302, status)
        self.assertEqual('/', redirect)

    def test_get(self):
        response = self.client.get(reverse('register'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_post_invalid(self):
        data = {
            'username': 'jo',
            'email': 'johjohn.om',
            'password1': 'saltking435',
            'password2': 'saltking45',
        }
        response = self.client.post(reverse('register'), data)
        status = response.status_code

        self.assertEqual(200, status)
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)

    def test_post_valid(self):
        data = {
            'username': 'rocky',
            'email': 'rara@rara.com',
            'password1': 'saltking45',
            'password2': 'saltking45',
        }
        response = self.client.post(reverse('register'), data)
        status = response.status_code
        redirect = response.headers['location']  # 'home'
        self.assertEqual(302, status)
        self.assertEqual('/', redirect)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)


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


class TestPasswordResetViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john',
                                             password='adidas1234',
                                             email='nozzller@gmail.com')

    def test_send_email(self):
        mail.send_mail(
            'Password reset',
            'Hello John!',
            'from@django.com',
            [self.user.email],
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password reset')
        self.assertEqual(mail.outbox[0].to, ['nozzller@gmail.com'])
        self.assertEqual(mail.outbox[0].from_email, 'from@django.com')
        self.assertEqual(mail.outbox[0].body, 'Hello John!')

    def test_password_reset_page(self):
        data = {
            'email': 'nozzller@gmail.com',
        }
        response = self.client.post(reverse('password_reset'), data)
        status = response.status_code
        self.assertEqual(302, status)
        redirect = response.headers['location']
        self.assertEqual('/accounts/password/reset/done/', redirect)

    def test_password_reset_confirm_page(self):
        default_token_generator = PasswordResetTokenGenerator()
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)

        data = {
            'new_password1': 'saltking45',
            'new_password2': 'saltking45',
        }
        response = self.client.post(reverse('password_reset_confirm',
                                            kwargs={'uidb64': uid, 'token': token}), data)
        status = response.status_code
        self.assertEqual(302, status)