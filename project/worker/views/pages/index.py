from django.utils.html import format_html


def create_category_list_html(categories):
    html = ''

    for category in categories:
        
        html += f"""
        <a class="box" href="/categorias/{ category.slug }">
            <div class="box-img-container">
                <img src="{ category.img.url }" alt="category-img" class="box-img">
            </div>
            <h2 class="box-title">{ category.name }</h2>
        </a>
        """

    return format_html(html)