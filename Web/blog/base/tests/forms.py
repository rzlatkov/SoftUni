from django.contrib.auth.models import User
from django.test import TestCase
from base.models import Post, Category
from base.forms import PostForm, CategoryForm, ProfileForm, CommentForm


class TestPostForm(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='john', password='adidas1234')
        self.category = Category.objects.create(name='Automotive')

    def test_post_invalid_title_too_short(self):
        data = {
            'title': 'A',
            'content': 'test',
            'category': [self.category],
            'snippet': 'something',
        }
        form = PostForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['Minimum length of 3 letters required.'])

    def test_post_invalid_title_fobidden_symbols(self):
        data = {
            'title': 'a23@',
            'content': 'test',
            'category': [self.category],
            'snippet': 'something',
        }
        form = PostForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['Only alphabet and whitespace characters are allowed.'])

    def test_post_valid(self):
        data = {
            'title': 'BMW',
            'content': 'test',
            'category': [self.category],
            'snippet': 'something',
        }
        form = PostForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(0, len(form.errors))


class TestCategoryForm(TestCase):
    def test_category_invalid_name_too_short(self):
        data = {
            'name': 'F'
        }
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Minimum length of 3 letters required.'])

    def test_category_invalid_name_no_capital_letter(self):
        data = {
            'name': 'food'
        }
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Invalid category name. First letter must be in CAPS.'])

    def test_category_invalid_name_forbidden_symbols(self):
        data = {
            'name': 'As124'
        }
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Only alphabet and whitespace characters are allowed.'])

    def test_category_valid_name(self):
        data = {
            'name': 'Travel'
        }
        form = CategoryForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(0, len(form.errors))


class TestCommentForm(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='john', password='adidas1234')
        self.category = Category.objects.create(name='Automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)

    def test_comment_invalid_name_forbidden_symbols(self):
        data = {
            'author': self.user,
            'name': 'asd1234f@',
            'content': 'test',
            'post': self.post,
        }
        form = CommentForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Only alphabet and whitespace characters are allowed.'])

    def test_comment_invalid_name_too_short(self):
        data = {
            'author': self.user,
            'name': 'A',
            'content': 'test',
            'post': self.post,
        }
        form = CommentForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Minimum length of 3 letters required.'])

    def test_comment_valid_name(self):
        data = {
            'author': self.user,
            'name': 'Arthur',
            'content': 'test',
            'post': self.post,
        }
        form = CommentForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(0, len(form.errors))


class TestProfileForm(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='john', password='adidas1234')

    def test_profile_location_invalid_too_short(self):
        data = {
            'username': 'rocky',
            'email': 'john@john.com',
            'first_name': 'john',
            'last_name': 'john',
            'location': 'A',
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['location'], ['Minimum length of 15 letters required.'])

    def test_profile_location_invalid_forbidden_symbols(self):
        data = {
            'username': 'rocky',
            'email': 'john@john.com',
            'first_name': 'john',
            'last_name': 'john',
            'location': 'A@fa2435!',
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())

    def test_profile_birth_date_in_the_future(self):
        data = {
            'username': 'rocky',
            'email': 'john@john.com',
            'first_name': 'john',
            'last_name': 'john',
            'birth_date': '2050-10-10',
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['birth_date'], ['Date cannot be present or in the future.'])

    def test_profile_birth_date_invalid_format(self):
        data = {
            'username': 'rocky',
            'email': 'john@john.com',
            'first_name': 'john',
            'last_name': 'john',
            'birth_date': 'A@fa2435!',
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['birth_date'], ['Enter a valid date.'])

    def test_profile_social_media_url_invalid(self):
        data = {
            'username': 'rocky',
            'email': 'john@john.com',
            'first_name': 'john',
            'last_name': 'john',
            'facebook_url': 'A',
        }
        form = ProfileForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['facebook_url'], ['Enter a valid URL.'])

    def test_profile_valid(self):
        data = {
            'username': 'rocky',
            'email': 'john@john.com',
            'first_name': 'john',
            'last_name': 'john',
            'facebook_url': 'facebook.com',
            'location': 'Sofia, Bulgaria'
        }
        form = ProfileForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(0, len(form.errors))