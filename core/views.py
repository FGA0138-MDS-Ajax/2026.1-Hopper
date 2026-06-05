from django.shortcuts import render


def home(request):
    """Renderiza a página inicial do HopLife."""

    return render(request, "home.html")

def acessibilidade_view(request):
    """Renderiza a página de acessibilidade."""
    return render(request, "acessibilidade.html")
