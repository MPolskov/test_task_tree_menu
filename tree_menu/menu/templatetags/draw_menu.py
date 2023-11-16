from django import template

from menu.models import MenuItem

register = template.Library


@register.inclusion_tag('menu/menu_item', takes_context=True)
def draw_menu(context, menu):
    menu_items = MenuItem.objects.filter(menu__title=menu).select_related('menu')
    

