from django.urls import path
from .pages import *


urlpatterns = [
    path('create', create_cache_data),
]