from django.shortcuts import render, redirect


BP = 'pages/' # base path




def category_view(request, category_name):
    return render(request, f'{BP}/categorias/[category_name].html')
