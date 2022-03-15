from Fast.utils.main import jsObj
from django.shortcuts import get_object_or_404, render, redirect
from backend.core import Project
from . import Category


BP = 'pages/' # base path




def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    projects = Project.objects.all()
    context = jsObj({
        'category',
        'projects',
    }, vars())
    return render(request, f'{BP}/categorias/[category_name].html', context)
