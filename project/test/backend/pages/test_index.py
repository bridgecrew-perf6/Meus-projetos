from django.test import TestCase, Client
from backend.categories import Category
from worker.views.manager import create_cache
from worker.views.pages.index import create_category_list_html



class TestIndex(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='test', slug='test',
            img='categories/python.png',
        )
        create_cache()
        self.request = self.client.get('/')

    def test_status(self):
        self.assertEqual(self.request.status_code, 200) 

    def test_main_content(self):
        category_list_html = str(create_category_list_html(Category.objects.all()))
        self.assertIn(category_list_html, str(self.request.content.decode('utf-8')))
