from django.utils.html import format_html



def create_category_pages(categories):
    pages = {}

    for category in categories:
        pages[category.slug] = format_html(create_bar_navigation(category) + create_project_list_box(category.projects.all()))
    
    return pages


def create_bar_navigation(category):
    html = f"""
    <nav class="bar-navigation">
        <a href="/">Projetos</a> &gt; <a href="/categorias/{ category.slug }">{ category.name }</a>
    </nav>
    """
    return html



def create_project_list(projects):
    html = ''
    for project in projects:
        html += f"""
            <a class="box" href="/projetos/{ project.slug }">
                <div class="box-img-container">
                    <img src="{ project.img.url }" alt="project-img" class="box-img">
                </div>
                <h2 class="box-title">{ project.name }</h2>
            </a>
        """
    return html


def create_project_list_box(projects):
    html = '<div class="box-container">' + create_project_list(projects) + '</div>'
    return html