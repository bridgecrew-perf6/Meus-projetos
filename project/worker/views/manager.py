from django.core.cache import cache

from worker.views.pages.projetos.project_slug import create_project_pages
from .support import create_context
from .pages.index import create_category_list_html
from .pages.categorias.category_slug import create_category_pages



def create_cache():

    context = create_context()

    cache_model = {

        'index': create_category_list_html(context['categories']),
        'categorias.category_slug': create_category_pages(context['categories']),
        'projetos.project_slug': create_project_pages(context['projects']),

    }

    cache.set_many(cache_model)
    for cache_key in cache_model.keys():
        cache.touch(cache_key, None)

    return cache_model




def update_cache():
    pass
