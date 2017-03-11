from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from mainpage.views import home_page

class HomePageTest(TestCase):

    def test_root_goes_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_contents(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Jason Zoller</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
