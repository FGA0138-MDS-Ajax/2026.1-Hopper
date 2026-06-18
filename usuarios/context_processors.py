# usuarios/context_processors.py

def configuracoes_acessibilidade(request):
    # Verifica se o usuário está logado e tem um perfil
    if request.user.is_authenticated and hasattr(request.user, 'perfil'):
        return {
            'global_tamanho_texto': request.user.perfil.tamanho_texto,
            'global_tamanho_botao': request.user.perfil.tamanho_botao,
        }
    # Valores padrão se o usuário não estiver logado
    return {
        'global_tamanho_texto': 'medio',
        'global_tamanho_botao': 'normal',
    }