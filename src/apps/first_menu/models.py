from django.db import models

class Menu(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class SubMenu(models.Model):
    name = models.CharField('Название пункта', max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255, null=True, blank=True)
    about = models.CharField('Интересный факт', max_length=255, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='menu_items', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Вариант меню'
        verbose_name_plural = 'Варианты меню'

    def __str__(self):
        return self.name
