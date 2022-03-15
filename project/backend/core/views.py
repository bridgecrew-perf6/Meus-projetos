from django.shortcuts import get_object_or_404, render, redirect
from Fast.utils.main import jsObj
from backend import categories
from backend.categories import Category
from backend.core import Project

BP = 'pages/' # base path


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, f'{BP}/index.html', context)


def project_view(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    category = project.category
    context = jsObj({
        'project',
        'category'
    }, vars())
    return render(request, f'{BP}/projetos/[project_slug].html', context)
