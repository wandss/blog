from django.db import models
from uuid import uuid4

#class PersonalLinks(models.Model):
#
#    link_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
#    name = models.CharField(max_length=30)
#    link = models.CharField(max_length=500)
#    icon = models.CharField(max_length=30, null=True, blank=True)


class Menu(models.Model):

    menu_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class AboutPage(models.Model):

    about_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=30)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class LandingPage(models.Model):

    landing_page_id = models.UUIDField(primary_key=True, editable=False,
            default=uuid4)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

#TODO:
# extend User model to have links

