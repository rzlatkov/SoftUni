from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from.forms import CreateUserForm, LoginUserForm, PasswordChangeFormBootstrap


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