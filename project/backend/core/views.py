from django.shortcuts import render, redirect
from backend import categories
from backend.categories import Category

BP = 'pages/' # base path


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, f'{BP}/index.html', context)