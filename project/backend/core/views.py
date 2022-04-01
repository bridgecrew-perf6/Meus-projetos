from django.shortcuts import render
from Fast.utils.main import get_cache_or_error, if_none
from django.views.decorators.cache import cache_page

BP = 'pages/' # base path


# @cache_page(60*5)
def index(request):
    from worker.views.manager import create_cache
    create_cache()
    context = {'category_list': get_cache_or_error('index')}
    return render(request, f'{BP}/index.html', context)


# @cache_page(60*5)
def project_view(request, project_slug):
    context = {'project_page': if_none(get_cache_or_error('projetos.project_slug').get(project_slug), '')}
    return render(request, f'{BP}/projetos/[project_slug].html', context)
