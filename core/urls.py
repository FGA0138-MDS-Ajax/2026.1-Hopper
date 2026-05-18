from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'), # A rota vazia aqui dentro do app core
]