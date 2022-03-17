from backend.categories import Category
from backend.core import Project


def create_context():
    context = {

        'categories': Category.objects.all().prefetch_related('projects'),
        'projects': Project.objects.all().select_related('category'),

    }

    return context