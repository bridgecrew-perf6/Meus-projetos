from Fast.utils.main import get_cache_or_error, if_none, jsObj
from django.shortcuts import get_object_or_404, render, redirect
from backend.core import Project
from . import Category


BP = 'pages/' # base path




def category_view(request, category_slug):
    context = {'category_page': if_none(get_cache_or_error('categorias.category_slug').get(category_slug), '')}
    return render(request, f'{BP}/categorias/[category_slug].html', context)
