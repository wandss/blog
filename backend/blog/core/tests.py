from io import StringIO

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.utils import timezone
from model_mommy import mommy
#from django.core.urlresolvers import reverse
from .models import Post

User = get_user_model()

class PostTest(TestCase):

    def test_create_post(self):

        post = mommy.make(Post)
        self.assertTrue(isinstance(post, Post))
        self.assertTrue(str(post), post.title)

class CreateDjangoAdminUserTest(TestCase):

    def test_create_superuser_command_output(self):
        out = StringIO()
        call_command('create_django_admin_user', stdout=out)
        self.assertIn('Created admin user', out.getvalue())



#coverage run manage.py test core -v 2


