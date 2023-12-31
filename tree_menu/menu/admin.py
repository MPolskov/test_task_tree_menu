from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug'
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'parent'
    )
    fieldsets = [
        (
            'Добавить',
            {
                'fields': (
                    'title',
                    'slug',
                    'menu',
                    'parent'
                )
            }
        )
    ]
