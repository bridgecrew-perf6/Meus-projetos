from django.contrib import admin
from project.Fast.django.decorators.cache.controler import renew_global_cache
from worker.views.manager import update_cache
from .models import Category


admin.site.empty_value_display = 'NULL'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = 'name',

    def save_model(self, request, obj, form, change):
        super(CategoryAdmin, self).save_model(request, obj, form, change)
        update_cache('index', 'categorias.category_slug')
        renew_global_cache('/')
        renew_global_cache(f'/categorias/{obj.slug}')
