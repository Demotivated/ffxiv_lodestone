from django.test import TestCase


class TrivialTestCase(TestCase):

    def test_nothing(self):
        self.assertTrue(True)
