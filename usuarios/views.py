from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import PerfilUsuario
from .services import REDIRECT_URI, keycloak_openid


def login_view(request):
    """Redirecionamento do user para a tela de autenticação do keycloak"""
    auth_url = keycloak_openid.auth_url(
        redirect_uri=REDIRECT_URI, scope="openid email profile"
    )

    auth_url = auth_url.replace("http://keycloak:8080/", "http://localhost:8080/")

    return redirect(auth_url)


def callback_view(request):
    """Recebe o código do Keycloak, valida e autentica o usuário no Django"""
    code = request.GET.get("code")

    if not code:
        return HttpResponseBadRequest("Código de autorização Inválido")
    try:
        # Troca o código temporário pelos tokens de acesso
        token_response = keycloak_openid.token(
            grant_type=["authorization_code"], code=code, redirect_uri=REDIRECT_URI
        )

        access_token = token_response["access_token"]

        # Recupera as informações do perfil do idoso (User info)
        user_info = keycloak_openid.userinfo(access_token)
        username = user_info["preferred_username"]
        email = user_info.get("email", "")
        first_name = user_info.get("given_name", "")
        keycloak_sub = user_info.get("sub")

        # Cria ou recupera o usuário na base local
        user, _ = User.objects.get_or_create(
            username=username, defaults={"email": email, "first_name": first_name}
        )

        # Cria o anexo com a id do keycloak
        PerfilUsuario.objects.get_or_create(
            usuario=user, defaults={"keycloak_id": keycloak_sub}
        )

        # Registra a sessão do usuário
        auth_login(request=request, user=user)

        # Redireciona para o dashboard principal
        return redirect("home")

    except Exception as e:
        # Tratamento genérico de erro
        return HttpResponse(f"Deu erro no callback {str(e)}")


def logout_view(request):
    """Termina a sessão no Django e limpa os cookies do Keycloak"""

    auth_logout(request)

    keycloak_logout_url = (
        "http://localhost:8080/realms/hoplife-realm/protocol/openid-connect/logout"
        "?client_id=hoplife-backend"
        "&post_logout_redirect_uri=http://localhost:8000/"
    )

    return redirect(keycloak_logout_url)


def acessibilidade_view(request):
    return render(request, "usuarios/acessibilidade.html")

@login_required # Garante que só quem tá logado acesse
def acessibilidade_view(request):
    perfil = request.user.perfil
    
    if request.method == 'POST':
        # Pega os valores selecionados no formulário HTML (usando o atributo 'name')
        novo_texto = request.POST.get('tamanho_letra')
        novo_botao = request.POST.get('tamanho_botao')
        
        # Validação básica de segurança
        if novo_texto in ['pequeno', 'medio', 'grande']:
            perfil.tamanho_texto = novo_texto
        if novo_botao in ['normal', 'largo']:
            perfil.tamanho_botao = novo_botao
            
        perfil.save()
        messages.success(request, 'Suas configurações de acessibilidade foram salvas!')
        return redirect('usuarios:acessibilidade') # Recarrega a página para atualizar visualmente
        
    # Envia os dados atuais do banco para preencher o formulário
    context = {
        'tamanho_texto': perfil.tamanho_texto,
        'tamanho_botao': perfil.tamanho_botao,
    }
    return render(request, "usuarios/acessibilidade.html", context)