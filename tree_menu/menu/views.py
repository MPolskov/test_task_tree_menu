from django.views.generic.base import TemplateView


class MenuView(TemplateView):
    """Класс представления меню."""
    template_name = 'menu/index.html'
