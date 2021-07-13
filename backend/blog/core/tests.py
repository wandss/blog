from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
#from django.core.urlresolvers import reverse
from .models import Post

User = get_user_model()

class PostTest(TestCase):

    def create_post(self, title="Some Post", tag="test",
            text="this is some content", author=User.objects.first(),
            publish_date=timezone.now()):

        return Post.objects.create(title=title, tag=tag, text=text,
                author=author, publish_date=publish_date
                )

    def test_create_post(self):

        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertTrue(str(post), post.title)

#coverage run manage.py test core -v 2


