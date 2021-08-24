from io import StringIO

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from model_mommy import mommy

from .models import Post
from .serializers import PostSerializer

User = get_user_model()
client = Client()

class PostTest(TestCase):

    def test_create_post(self):

        post = mommy.make(Post)
        self.assertTrue(isinstance(post, Post))
        self.assertTrue(str(post), post.title)

class GetAllPosts(TestCase):
    """Test Post API"""

    def setUp(self):
       self.post = mommy.make(Post)
       self.post_1 = mommy.make(Post)
       self.post_2 = mommy.make(Post)

    def test_gell_all_posts(self):
        response = client.get(reverse('get_create_posts'))
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_get_single_post(self):
        response = client.get(reverse('get_post',
            kwargs={'post_id':self.post.post_id}))
        serializer = PostSerializer(self.post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_create_post(self):
        response = client.post(reverse)


class CreateDjangoAdminUserTest(TestCase):

    def test_create_superuser_command_output(self):
        out = StringIO()
        call_command('create_django_admin_user', stdout=out)
        self.assertIn('Created admin user', out.getvalue())




#coverage run manage.py test core -v 2


