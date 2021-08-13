from django.contrib.auth.models import User
from django.test import TestCase
from base.models import Post, Category, Comment, Profile


class TestPostModel(TestCase):
    def test_post_model(self):
        user = User.objects.create_user(username='john', password='adidas1234')
        category = Category.objects.create(name='Automotive')
        post = Post.objects.create(title='BMW', author=user, snippet='vrumvrum')
        post.category.add(category)
        self.assertEqual(post.author.pk, user.pk)
        self.assertEqual(post.author.username, user.username)


class TestCategoryModel(TestCase):
    def test_category_model(self):
        category = Category.objects.create(name='Automotive')
        qs = Category.objects.first()
        self.assertEqual(qs.name, category.name)


class TestCommentModel(TestCase):
    def test_comment_model(self):
        user = User.objects.create_user(username='john', password='adidas1234')
        category = Category.objects.create(name='Automotive')
        post = Post.objects.create(title='BMW', author=user, snippet='vrumvrum')
        post.category.add(category)
        comment = Comment.objects.create(author=user, name='asdasd', content='test', post=post)
        self.assertEqual(comment.post.pk, post.pk)
        self.assertEqual(comment.author.pk, user.pk)
        cat = post.category.first()
        self.assertEqual(cat.name, category.name)


class TestProfileModel(TestCase):
    def test_profile_upon_user_creation(self):
        user = User.objects.create_user(username='john', password='adidas1234')
        user_profile = user.profile
        profile = Profile.objects.first()
        self.assertEqual(profile.pk, user.pk)
        self.assertEqual(user_profile.pk, profile.pk)
        self.assertEqual('john', profile.user.username)