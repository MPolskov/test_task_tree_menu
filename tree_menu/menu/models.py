from django.db import models


class Menu(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название меню'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Адрес'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название пункта'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Адрес'
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu',
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Родительская ветка'
    )

    class Meta:
        verbose_name = 'Ветка Меню'
        verbose_name_plural = 'Ветки Меню'

    def __str__(self):
        return self.title
