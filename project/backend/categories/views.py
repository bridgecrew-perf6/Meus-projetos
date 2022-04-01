from Fast.utils.main import get_cache_or_error, if_none
from django.shortcuts import render
from django.views.decorators.cache import cache_page


BP = 'pages/' # base path



# @cache_page(60*5)
def category_view(request, category_slug):
    context = {'category_page': if_none(get_cache_or_error('categorias.category_slug').get(category_slug), '')}
    return render(request, f'{BP}/categorias/[category_slug].html', context)
