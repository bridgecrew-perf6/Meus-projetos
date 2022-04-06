from django.utils.html import format_html



def create_project_pages(projects):
    pages = {}

    for project in projects:
        pages[project.slug] = format_html(create_navigation(project) + create_project_data_html(project))

    return pages


def create_navigation(project):
    html = f"""
    <nav class="bar-navigation">
        <a href="/">Categorias</a> &gt; <a href="/categorias/{ project.category.slug }">{ project.category.name }</a> &gt; <a href="/projetos/{ project.slug }">{ project.name }</a>
    </nav>
    """
    return html


def create_project_url_html(project):
    html = f"""
    <div class="project-info">
        <label for="" class="project-label">Link projeto:</label>
        <a  href="{ project.project_url }" class="project-name" target="_blank">{ project.project_url }</a>
    </div>
    """
    return html


def create_project_data_html(project):
    project_url_html = create_project_url_html(project) if project.project_url != '' else ''
    html = f"""
    <h1 class="title">{ project.name }</h1>
    <div class="img-project">
        <img src="{ project.img.url }" alt="img-project">
    </div>
    <div class="project-info">
        <label for="" class="project-label">Categoria:</label>
        <span class="project-name">{ project.category.name }</span>
    </div>
    {project_url_html}
    <div class="project-info">
        <label for="" class="project-label">Link Github:</label>
        <a href="{ project.github_url }" class="project-name" target="_blank">{ project.github_url }</a>
    </div>
    """
    return html
