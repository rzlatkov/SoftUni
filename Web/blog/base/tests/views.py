from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from base.models import Post, Category, Comment


class TestPostLikeView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)

    def test_not_logged_in(self):
        response = self.client.post(reverse('post-like', kwargs={'pk': self.post.pk}))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/post/like/{self.post.pk}', redirect)

    def test_post_not_found(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('post-like', kwargs={'pk': 10}))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)
        self.assertEqual(404, status)

    def test_like(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('post-like', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(302, status)
        self.assertEqual(1, self.post.likes_count())

    def test_unlike(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('post-like', kwargs={'pk': self.post.pk}))
        self.assertEqual(1, self.post.likes_count())
        response = self.client.post(reverse('post-like', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(302, status)
        self.assertEqual(0, self.post.likes_count())


class TestCommentAddView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)

    def test_not_logged_in(self):
        response = self.client.get(reverse('comment-add', kwargs={'pk': self.post.pk}))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/comment/add/{self.post.pk}', redirect)

    def test_request_method_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('comment-add', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(200, status)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_request_method_post_invalid_form(self):
        self.client.force_login(self.user)
        data = {
            'name': '23',
            'content': 'invalid name',
        }
        response = self.client.post(reverse('comment-add', kwargs={'pk': self.post.pk}), data)
        status = response.status_code
        self.assertEqual(200, status)
        self.assertEqual(0, self.post.comments.count())

    def test_request_method_post_valid_form(self):
        self.client.force_login(self.user)
        data = {
            'name': 'rocky',
            'content': 'invalid name',
        }
        response = self.client.post(reverse('comment-add', kwargs={'pk': self.post.pk}), data)
        redirect = response.headers['location']
        status = response.status_code
        self.assertEqual(302, status)
        self.assertEqual(f'/post/{self.post.pk}', redirect)
        self.assertEqual(1, self.post.comments.count())


class TestCommentEditView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)
        self.comment = Comment.objects.create(author=self.user, name='rocky', content='asdasd', post=self.post)

    def test_not_logged_in(self):
        response = self.client.get(reverse('comment-edit', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/comment/edit/{self.comment.pk}', redirect)

    def test_request_method_get_valid_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('comment-edit', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        self.assertEqual(200, status)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_request_method_get_invalid_permission(self):
        user_2 = User.objects.create_user(username='statham', password='adidas1234')
        self.client.force_login(user_2)
        response = self.client.get(reverse('comment-edit', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        self.assertEqual(403, status)

    def test_request_method_post_valid_form(self):
        self.client.force_login(self.user)
        data = {
            'name': 'roy',
            'content': 'changed',
        }
        response = self.client.post(reverse('comment-edit', kwargs={'pk': self.comment.pk}), data)
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/post/{self.comment.post.pk}', redirect)

    def test_request_method_post_invalid_form(self):
        self.client.force_login(self.user)
        data = {
            'name': 'r12412y',
            'content': 'changed',
        }
        response = self.client.post(reverse('comment-edit', kwargs={'pk': self.comment.pk}), data)
        status = response.status_code
        self.assertEqual(200, status)


class TestCommentDeleteView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)
        self.comment = Comment.objects.create(author=self.user, name='rocky', content='asdasd', post=self.post)

    def test_not_logged_in(self):
        response = self.client.get(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/comment/delete/{self.comment.pk}', redirect)

    def test_request_method_get_valid_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        self.assertEqual(200, status)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_request_method_get_invalid_permission(self):
        user_2 = User.objects.create_user(username='statham', password='adidas1234')
        self.client.force_login(user_2)
        response = self.client.get(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        self.assertEqual(403, status)

    def test_request_method_post(self):
        self.client.force_login(self.user)
        self.assertEqual(1, self.post.comments.count())
        response = self.client.post(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/post/{self.post.pk}', redirect)
        self.assertEqual(0, self.post.comments.count())


class TestCategoryDetailView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='Automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)
        self.post_2 = Post.objects.create(title='audi', author=self.user, snippet='idkkk')
        self.post_2.category.add(self.category)

    def test_category_with_posts(self):
        response = self.client.get('/category/automotive')
        status = response.status_code
        self.assertEqual(200, status)
        post_2 = Post.objects.create(title='audi', author=self.user, snippet='idkkk')
        post_2.category.add(self.category)
        self.assertEqual(2, len(response.context['posts_by_cat']))

    def test_category_without_posts(self):
        cat_2 = Category.objects.create(name='Travel')
        response = self.client.get('/category/travel')
        status = response.status_code
        self.assertEqual(200, status)
        self.assertEqual(0, len(response.context['posts_by_cat']))

    def test_category_not_found(self):
        response = self.client.get('/category/notthere')
        status = response.status_code
        self.assertEqual(404, status)


class TestCategoryAddView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.user.is_staff = True
        self.user.save()

    def test_not_logged_in(self):
        response = self.client.get(reverse('category-add'))
        status = response.status_code
        user = auth.get_user(self.client)
        self.assertTrue(not user.is_authenticated)
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/category/add/', redirect)

    def test_logged_in_no_staff(self):
        self.user.is_staff = False
        self.user.save()
        self.client.force_login(self.user)
        response = self.client.get(reverse('category-add'))
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/admin/login/?next=/category/add/', redirect)

    def test_logged_in_staff_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('category-add'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_logged_in_staff_post_invalid_form(self):
        self.client.force_login(self.user)
        data = {
            'name': 'n0',
        }
        response = self.client.post(reverse('category-add'), data)
        status = response.status_code
        self.assertEqual(200, status)
        self.assertEqual(0, Category.objects.all().count())

    def test_logged_in_staff_post_valid_form(self):
        self.client.force_login(self.user)
        data = {
            'name': 'Voodoo',
        }
        response = self.client.post(reverse('category-add'), data)
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(f'/categories/', redirect)
        self.assertEqual(302, status)
        self.assertEqual(1, Category.objects.all().count())


class TestCategoryListView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.category = Category.objects.create(name='Automotive')
        self.category2 = Category.objects.create(name='Travel')

    def test_list_without_search(self):
        response = self.client.get(reverse('category-list'))
        self.assertIn('page_obj', response.context)
        self.assertEqual(2, len(response.context['page_obj']))

    def test_list_search_found(self):
        data = {
            'q': 'tra',
        }
        response = self.client.get(reverse('category-list'), data)
        self.assertIn('page_obj', response.context)
        self.assertEqual(1, len(response.context['page_obj']))

    def test_list_search_nothing_found(self):
        data = {
            'q': 'qwdafswdaw',
        }
        response = self.client.get(reverse('category-list'), data)
        self.assertIn('page_obj', response.context)
        self.assertEqual(0, len(response.context['page_obj']))


class TestHomeView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='Automotive')
        self.category2 = Category.objects.create(name='Electronics')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)
        self.post_2 = Post.objects.create(title='audi', author=self.user, snippet='idkkk')
        self.post_2.category.add(self.category2)

    def test_without_search(self):
        response = self.client.get(reverse('home'))
        self.assertIn('page_obj', response.context)
        self.assertEqual(2, len(response.context['page_obj']))

    def test_with_search_found(self):
        data = {
            'q': 'electro'
        }
        response = self.client.get(reverse('home'), data)
        self.assertIn('page_obj', response.context)
        self.assertEqual(1, len(response.context['page_obj']))

    def test_with_search_nothing_found(self):
        data = {
            'q': 'ugabugabakerolls'
        }
        response = self.client.get(reverse('home'), data)
        self.assertIn('page_obj', response.context)
        self.assertEqual(0, len(response.context['page_obj']))


class TestPostView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='Automotive')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)

    def test_post_details(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(200, status)
        self.assertIn('post', response.context)
        obj = response.context.get('post')
        self.assertEqual('BMW', obj.title)
        self.assertEqual('vrumvrum', obj.snippet)


class TestAddPostView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='Automotive')
        self.category2 = Category.objects.create(name='Electronics')

    def test_not_logged_in(self):
        response = self.client.get(reverse('post-add'))
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual('/accounts/login/?next=/post/add/', redirect)

    def test_logged_in_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('post-add'))
        status = response.status_code
        self.assertEqual(200, status)

    def test_logged_in_post_valid_form(self):
        self.client.force_login(self.user)
        data = {
            'title': 'tesla',
            'content': 'EVs',
            'category': self.category.pk,
            'snippet': 'hope it runs',
        }
        response = self.client.post(reverse('post-add'), data)
        status = response.status_code
        self.assertEqual(302, status)
        post = Post.objects.last()
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.title, 'tesla')

    def test_logged_in_test_invalid_form(self):
        self.client.force_login(self.user)
        data = {
            'title': '123a',
            'content': 'EVs',
            'category': self.category.pk,
            'snippet': 'hope it runs',
        }
        response = self.client.post(reverse('post-add'), data)
        status = response.status_code
        self.assertEqual(200, status)
        self.assertEqual(Post.objects.count(), 0)


class TestUpdatePostView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='Automotive')
        self.category2 = Category.objects.create(name='Electronics')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)

    def test_not_logged_in(self):
        response = self.client.get(reverse('post-edit', kwargs={'pk': self.post.pk}))
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/post/edit/{self.post.pk}', redirect)

    def test_logged_in_personal_content(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('post-edit', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(200, status)

    def test_logged_in_non_personal_content(self):
        self.user2 = User.objects.create_user(username='rocky', password='saltking45')
        self.client.force_login(self.user2)
        response = self.client.get(reverse('post-edit', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(403, status)

    def test_logged_in_post_valid_form(self):
        self.client.force_login(self.user)
        data = {
            'title': 'AUDI',
            'content': 'EVs',
            'category': self.category2.pk,
            'snippet': 'hope it runs',
        }
        response = self.client.post(reverse('post-edit', kwargs={'pk': self.post.pk}), data)
        status = response.status_code
        self.assertEqual(302, status)
        post = Post.objects.last()
        self.assertEqual('AUDI', post.title)
        self.assertEqual('hope it runs', post.snippet)
        self.assertEqual(1, Post.objects.count())

    def test_logged_in_post_invalid_form(self):
        self.client.force_login(self.user)
        data = {
            'title': '3s',
            'content': '@@@',
            'category': self.category2.pk,
            'snippet': 'hope it runs',
        }
        response = self.client.post(reverse('post-edit', kwargs={'pk': self.post.pk}), data)
        status = response.status_code
        self.assertEqual(200, status)
        post = Post.objects.last()
        self.assertEqual('BMW', post.title)
        self.assertEqual('vrumvrum', post.snippet)


class TestDeletePostView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='saltking45')
        self.category = Category.objects.create(name='Automotive')
        self.category2 = Category.objects.create(name='Electronics')
        self.post = Post.objects.create(title='BMW', author=self.user, snippet='vrumvrum')
        self.post.category.add(self.category)

    def test_not_logged_in(self):
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual(302, status)
        self.assertEqual(f'/accounts/login/?next=/post/delete/{self.post.pk}', redirect)

    def test_logged_in_personal_content(self):
        self.client.force_login(self.user)
        self.assertEqual(1, Post.objects.count())
        response = self.client.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        status = response.status_code
        redirect = response.headers['location']
        self.assertEqual('/', redirect)
        self.assertEqual(302, status)
        self.assertEqual(0, Post.objects.count())

    def test_logged_in_non_personal_content(self):
        self.user2 = User.objects.create_user(username='rocky', password='saltking45')
        self.client.force_login(self.user2)
        response = self.client.get(reverse('post-delete', kwargs={'pk': self.post.pk}))
        status = response.status_code
        self.assertEqual(403, status)