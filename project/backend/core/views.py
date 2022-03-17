from django.shortcuts import get_object_or_404, render, redirect
from Fast.utils.main import get_cache_or_error, if_none, jsObj
from backend.core import Project

BP = 'pages/' # base path


def index(request):
    context = {'category_list': get_cache_or_error('index')}
    return render(request, f'{BP}/index.html', context)


def project_view(request, project_slug):
    context = {'project_page': if_none(get_cache_or_error('projetos.project_slug').get(project_slug), '')}
    return render(request, f'{BP}/projetos/[project_slug].html', context)
