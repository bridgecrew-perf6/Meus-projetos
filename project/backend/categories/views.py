from django.shortcuts import get_object_or_404, render, redirect
from . import Category

BP = 'pages/' # base path




def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = {'category': category}
    return render(request, f'{BP}/categorias/[category_name].html', context)
