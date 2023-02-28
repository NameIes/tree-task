from django import template
from django.shortcuts import get_object_or_404

from tree.models import TreeMenu

register = template.Library()


@register.simple_tag(name='draw_menu')
def draw_menu(menu_name):
    context ={
        'menu': get_object_or_404(TreeMenu, name=menu_name)
    }
    return template.loader.render_to_string('draw_menu.html', context)
