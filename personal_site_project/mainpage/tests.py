from django.test import TestCase

class NotFailMathTest(TestCase):

    def test_love_the_leader(self):
        self.assertEqual(2 + 2, 5)
