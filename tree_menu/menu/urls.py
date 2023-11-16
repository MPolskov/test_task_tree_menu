from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path(
        'menu/<slug:slug>/',
        views.MenuView.as_view(),
        name='menu'
    ),
]
