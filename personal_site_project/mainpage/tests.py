from django.test import TestCase
from django.core.urlresolvers import resolve
from mainpage.views import home_page

class HomePageTest(TestCase):

    def test_root_goes_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
