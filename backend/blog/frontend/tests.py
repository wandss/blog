from django.test import TestCase
from django.utils import timezone
from .models import Menu, AboutPage, LandingPage
from model_mommy import mommy


class MenuTest(TestCase):

    def test_create_menu(self):
        menu = mommy.make(Menu)
        self.assertTrue(isinstance(menu, Menu))
        self.assertTrue(str(menu), menu.name)


class AboutPageTest(TestCase):

    def test_create_about_page(self):
        about_page = mommy.make(AboutPage)
        self.assertTrue(isinstance(about_page, AboutPage))
        self.assertTrue(str(about_page), about_page.title)


class LandingPageTest(TestCase):

    def test_create_landing_page(self):
        landing_page = mommy.make(LandingPage)
        self.assertTrue(isinstance(landing_page, LandingPage))
        self.assertTrue(str(landing_page), landing_page.title)
