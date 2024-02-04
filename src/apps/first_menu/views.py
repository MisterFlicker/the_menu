from django.shortcuts import render
from .models import SubMenu


def base(request):
    return render(
        request,
        'base.html',
        {'main_menu': SubMenu.objects.filter(parent__name=None)}
    )


def get_menu(request, path):
    path = path.replace('_', ' ')
    splitted_path = path.split('/')
    tree = []

    for i in splitted_path:
        tree.append(i)

    return render(
        request,
        'base.html',
        {'tree': tree}
    )
