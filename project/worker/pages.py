from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from .views.manager import create_cache

def create_cache_data(request):
    model = create_cache()
    return JsonResponse(model)