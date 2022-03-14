from django.urls import path
from .views import *


urlpatterns = [
    path('<slug:category_slug>', category_view, name='category_view'),
]
