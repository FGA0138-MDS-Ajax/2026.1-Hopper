from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login_view(request):
    """
    Renderiza a view de login provisória.
    """
    return HttpResponse("Página de Login (Em Construção)")


def registro_view(request):
    """
    Renderiza a view de registro provisória.
    """
    return HttpResponse("Página de Registro (Em Construção)")

