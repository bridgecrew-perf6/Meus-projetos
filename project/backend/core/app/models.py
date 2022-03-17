from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, SlugField, CASCADE)
from backend.categories import Category



class Project(Model):
    name = CharField(verbose_name='Nome', max_length=128)
    slug = SlugField(verbose_name='Url', max_length=256)
    img = ImageField(verbose_name='Img', upload_to='project/%Y/%m/%d')
    project_url = TextField(verbose_name='Url do projeto', blank=True, null=True)
    github_url = TextField(verbose_name='Url do Github')
    category = ForeignKey(Category, related_name='projects', on_delete=CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'


