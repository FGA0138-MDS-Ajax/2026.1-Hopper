def acessibilidade_context(request):
    """
    Injeta as preferências de acessibilidade do PerfilUsuario em todos os templates de forma global.
    """
    if request.user.is_authenticated:
        try:
            # Acessa através do related_name 'perfil' definido no OneToOneField
            perfil = request.user.perfil
            return {
                'tamanho_texto': perfil.tamanho_texto,
                'tamanho_botao': perfil.tamanho_botao,
                'assistencia_motora': perfil.assistencia_motora_ativa,
            }
        except Exception:
            pass
            
    return {
        'tamanho_texto': 'medio',
        'tamanho_botao': 'normal',
        'assistencia_motora': False,
    }
