from django.urls import path

from .views import home, acessibilidade_view

urlpatterns = [
    path("", home, name="home"),
    path("acessibilidade/", acessibilidade_view, name="acessibilidade"),
]
