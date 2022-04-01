from django.shortcuts import render
from Fast.utils.main import get_cache_or_error, if_none
from Fast.django.decorators.cache.main import static_page

BP = 'pages/' # base path


@static_page
def index(request):
    context = {'category_list': get_cache_or_error('index')}
    return render(request, f'{BP}/index.html', context)


@static_page
def project_view(request, project_slug):
    context = {'project_page': if_none(get_cache_or_error('projetos.project_slug').get(project_slug), '')}
    return render(request, f'{BP}/projetos/[project_slug].html', context)
