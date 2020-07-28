from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class HomePageViewTest(TestCase):
    def test_home_page_status_check(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/home.html')


class PostModelTest(TestCase):

    def setUp(self):
        self.author = get_user_model().objects.create_user(
            username="test",
            email='test@company.com',
            password="test123456")

        self.post = Post.objects.create(
            title="test_post",
            content="test content",
            author=self.author)

    def test_string_representation(self):
        post = Post.objects.first()
        self.assertEqual(str(post), 'test_post')

    def test_description(self):
        post = Post.objects.first()
        self.assertEqual(post.content, "test content")
