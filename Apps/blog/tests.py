from django.test import TestCase
# 测试工具的默认在以 test 开头的文件中找到所有的 unittest.TestCase 的子类，从这些测试用例中自动构建一个测试套件，然后运行该套件
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