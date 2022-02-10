from django.test import TestCase
from django.urls import reverse
from posts.models import Post

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text = 'just a simple test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a simple test')

class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text = 'it is another simple text' )

    def test_view_url_exists(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('HomePage'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')