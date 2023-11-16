from django.views.generic.base import TemplateView


class MenuView(TemplateView):
    """Класс представления страницы меню"""
    template_name = 'menu/index.html'


