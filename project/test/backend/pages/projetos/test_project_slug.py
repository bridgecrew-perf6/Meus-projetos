from django.test import TestCase, Client
from backend.categories import Category
from backend.core.app.models import Project
from worker.views.manager import create_cache
from worker.views.pages.categorias.category_slug import create_project_list, create_project_list_box
from worker.views.pages.projetos.project_slug import create_project_data_html



class TestProjectPage(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='test', slug='test',
            img='categories/python.png',
        )
        self.project = Project(
            name='test', slug='test',
            img='project/2022/03/14/p1.JPG',
            project_url='test.com',
            github_url='test.com',
            category=self.category,
        )
        self.project.save()
        create_cache()
        self.request = self.client.get(f'/projetos/{self.project.slug}')

    def test_status(self):
        self.assertEqual(self.request.status_code, 200) 

    def test_main_content(self):
        projects_page_html = str(create_project_data_html(self.project))
        self.assertIn(projects_page_html, str((self.request.content).decode('utf-8')))