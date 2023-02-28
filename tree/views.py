from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import TreeItem, TreeMenu


def index(request):
    return render(request, 'index.html')


def get_items_with_opened(items, open_ids, __i=0):
    if not open_ids:
        return items

    result = []
    for item in items:
        dict_item = {
            'obj': item,
            'opened': False,
            'childs': [],
        }

        try:
            if item.id == open_ids[__i]:
                dict_item['opened'] = True
                dict_item['childs'] = get_items_with_opened(item.childrens.all(), open_ids, __i+1)
        except IndexError:
            childs = item.childrens.all()
            if childs:
                dict_item['opened'] = True
                for child in childs:
                    dict_item['childs'].append({
                        'obj': child,
                        'opened': False,
                        'childs': []
                    })

        result.append(dict_item)

    return result


def item_existence_check(items_id):
    for i in items_id:
        get_object_or_404(TreeItem, id=i)


def menu(request, menu_id, path=None):
    tree_menu = get_object_or_404(TreeMenu, id=menu_id)
    items_id = None
    if path:
        items_id = [int(i) for i in path.split('/') if i]
        item_existence_check(items_id)
    context = {
        'menu': tree_menu,
        'items': get_items_with_opened(tree_menu.childrens.all(), items_id)
    }

    return render(request, 'menu.html', context)