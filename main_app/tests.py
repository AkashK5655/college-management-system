
from django.test import TestCase


class BasicCMSTest(TestCase):

    def test_basic_assertion(self):
        self.assertEqual(1 + 1, 2)
