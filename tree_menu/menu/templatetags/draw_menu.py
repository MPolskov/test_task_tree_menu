from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu_item.html', takes_context=True)
def draw_menu(context, menu):
    menu_items = MenuItem.objects.filter(menu__slug=menu).select_related('menu')
    # menu_items_values = menu_items.values()
    base_items = menu_items.filter(parent=None).values()
    selected_item = menu_items.get(slug=context['slug'])
    selected_items_list = get_item_list(selected_item)

    for item in base_items:
        if item['id'] in selected_items_list:
            item['children'] = get_children(menu_items, selected_items_list, item['id'])
    result = {
        'items': base_items
    }
    return result


def get_item_list(selected_item):
    node_items_list = []
    while selected_item:
        node_items_list.append(selected_item.id)
        selected_item = selected_item.parent
    return node_items_list


def get_children(menu_items, selected_items_list, item_id):
    children_list = [item for item in menu_items.filter(parent_id=item_id).values()]
    for item in children_list:
        if item['id'] in selected_items_list:
            item['children'] = get_children(menu_items, selected_items_list, item['id'])
    return children_list
