from django.contrib import admin

from worker.views.manager import update_cache
from .models import Project

admin.site.empty_value_display = 'NULL'




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = 'name', 'slug', 
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = 'name',

    def save_model(self, request, obj, form, change):
        super(ProjectAdmin, self).save_model(request, obj, form, change)
        update_cache('projetos.project_slug', 'categorias.category_slug')
