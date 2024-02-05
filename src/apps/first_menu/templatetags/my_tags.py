from django import template
from apps.first_menu.models import SubMenu

register = template.Library()


@register.inclusion_tag('sub_menu.html')
def get_sub_menu(tree):
    """Функция, описывающая подменю.
    tree - путь до выбранного пункта меню в виде списка.
    """
    x = []
    y = SubMenu.objects.all()

    for branch in reversed(tree):

        if branch == tree[-1]:
            current_item = branch

            if y.filter(parent__name=branch):
                x.append(list(y.filter(parent__name=branch)))

        x.append(list(y.filter(name=branch)))

    return {'sub_menu': reversed(x), 'current_item': current_item}


@register.simple_tag()
def multiply(a):
    """Функция для создания отступов для подменю, возвращая количество пикселей в отступе.
    a - counter цикла, перебирающего пункты меню
    """
    return a * 25
