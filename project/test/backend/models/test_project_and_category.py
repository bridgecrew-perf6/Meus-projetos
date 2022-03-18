from django.test import TestCase
from unittest import expectedFailure
from backend.core.app.models import Project
from backend.categories.app.models import Category




class TestProjectModel(TestCase):

    def setUp(self):
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

    def test_relationship_fk(self):
        self.assertEqual(self.category, self.project.category)

    def test_relationship_many_to_1(self):
        self.assertEqual(list(self.category.projects.all()), [self.project])
