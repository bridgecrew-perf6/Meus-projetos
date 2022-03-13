from django.urls import path
from .views import *


urlpatterns = [
    path('<slug:category_name>', category_view, name='category_view'),
]
