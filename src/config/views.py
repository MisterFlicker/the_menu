from django.shortcuts import render
from apps.first_menu.models import SubMenu
from .default_menu import fill_default_menu


def index(request):
    """Функция, обрабатывающая заглавный экран проекта.
    Также происходит проверка наличия записей в БД и, в случае отсутствия, возвращает True статус об этом.

    """
    empty_menu = True

    if SubMenu.objects.all():
        empty_menu = False

    return render(
        request,
        'index.html',
        {'empty_menu': empty_menu}
    )


def fill_menu(request):
    """Функция, обрабатывающая заполнение БД данными по умолчанию."""
    fill_default_menu()
    return render(
        request,
        'base.html',
        {'main_menu': SubMenu.objects.filter(parent__name=None)}
    )


def delete_menu(request):
    """Функция, обрабатывающая удаление всех данных из БД."""
    SubMenu.objects.all().delete()
    return render(
        request,
        'index.html',
        {'empty_menu': True}
    )
