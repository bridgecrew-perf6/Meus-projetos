from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('projetos/<slug:project_slug>', project_view, name='project_view'),
]
