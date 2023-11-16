from django.shortcuts import render


def index(request):
    """Функция представления главной страницы"""
    template = 'menu/index.html'
    return render(request, template)
