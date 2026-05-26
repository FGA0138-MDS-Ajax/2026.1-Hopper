from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from .models import PerfilUsuario
from .services import REDIRECT_URI, keycloak_openid


def login_view(request):
    """Renderiza página de login com botão para autenticação do Keycloak"""
    auth_url = keycloak_openid.auth_url(
        redirect_uri=REDIRECT_URI, scope="openid email profile"
    )

    auth_url = auth_url.replace("http://keycloak:8080/", "http://localhost:8080/")

    context = {
        "login_url": auth_url
    }
    
    return render(request, "login.html", context)


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

        # Renderiza página de sucesso
        context = {
            "user": user
        }
        return render(request, "success.html", context)

    except Exception as e:
        # Tratamento genérico de erro
        return HttpResponse(f"Deu erro no callback {str(e)}")


def logout_view(request):
    """Termina a sessão no Django e renderiza página de logout"""

    auth_logout(request)

    # Renderiza página de logout com informações
    return render(request, "logout.html")
