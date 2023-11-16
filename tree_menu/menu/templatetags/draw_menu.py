from django import template

from menu.models import MenuItem

register = template.Library

@register.inclusion_tag('menu/menu_item')
def draw_menu(menu):
    menu_items = MenuItem.objects.filter(menu__title=menu).select_related('menu')
    