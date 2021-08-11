from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


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