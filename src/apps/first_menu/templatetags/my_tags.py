from django import template
from apps.first_menu.models import SubMenu

register = template.Library()


@register.inclusion_tag('sub_menu.html')
def get_sub_menu(tree):
    x = []
    y = SubMenu.objects.all()
    for branch in reversed(tree):
        if branch == tree[-1]:
            if y.filter(parent__name=branch):
                x.append(list(y.filter(parent__name=branch)))
        x.append(list(y.filter(name=branch)))
    return {'sub_menu': reversed(x)}


@register.simple_tag()
def multiply(a, b, *args, **kwargs):
    return a * 6 * b + '>'
