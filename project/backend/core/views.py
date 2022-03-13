from django.shortcuts import render, redirect


BP = 'pages/' # base path


def index(request):
    return render(request, f'{BP}/index.html')