from django.shortcuts import render

def home(request):
    """
    Renderiza a página inicial do HopLife.
    """
    return render(request, 'home.html')