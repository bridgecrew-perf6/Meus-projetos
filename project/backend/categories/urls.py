from django.urls import path
from .views import *


urlpatterns = [
    path('', categories_list, name='categories_list'),
    path('<slug:category_name>', category_view, name='category_view'),
]
