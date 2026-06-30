from django.shortcuts import render
from gamificacao.models import FraseInspiradora

def home(request):
    """Renderiza a página inicial do HopLife."""
    
    # Faz o sorteio de uma frase aleatória no banco de dados
    frase_sorteada = FraseInspiradora.objects.order_by("?").first()
    
    # Cria o contexto com os dados que vão para a tela
    contexto = {
        "frase_do_dia": frase_sorteada,
    }

    # Envia o contexto junto com o HTML
    return render(request, "home.html", contexto)