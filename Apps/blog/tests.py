from django.test import TestCase
from .models import *
# Create your tests here.


class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(title="lion", body="111111111111111111111")
        Blog.objects.create(title="cat", body="222222222222222222222")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Blog.objects.get(name="lion")
        cat = Blog.objects.get(name="cat")
        self.assertEqual(lion.get_absolute_url(), 'The lion says "roar"')
        self.assertEqual(cat.get_absolute_url(), 'The cat says "meow"')