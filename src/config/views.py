from django.shortcuts import render
from apps.first_menu.models import SubMenu
from .default_menu import fill_default_menu

def index(request):
    empty_menu = True
    if SubMenu.objects.all():
        empty_menu = False
    return render(
        request,
        'index.html',
        {'empty_menu': empty_menu}
    )

def fill_menu(request):
    fill_default_menu()
    return render(
        request,
        'base.html',
        {'main_menu': SubMenu.objects.filter(parent__name=None)}
    )


def delete_menu(request):
    SubMenu.objects.all().delete()
    empty_menu = True
    if SubMenu.objects.all():
        empty_menu = False
    return render(
        request,
        'index.html',
        {'empty_menu': empty_menu}
    )
