from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from .models import PerfilUsuario
from .services import REDIRECT_URI, keycloak_openid


def login_view(request):
    """Exibe a página de login e prepara o link de autenticação do Keycloak."""
    auth_url = keycloak_openid.auth_url(
        redirect_uri=REDIRECT_URI, scope="openid email profile"
    )

    auth_url = auth_url.replace("http://keycloak:8080/", "http://localhost:8080/")

    return render(request, "usuarios/login.html", {"auth_url": auth_url})


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

        # Renderiza a página de callback após autenticar o usuário
        return render(request, "usuarios/callback.html", {"user": user})

    except Exception as e:
        # Tratamento genérico de erro
        return HttpResponse(f"Deu erro no callback {str(e)}")


def logout_view(request):
    """Termina a sessão no Django e renderiza a página de logout."""

    auth_logout(request)

    keycloak_logout_url = (
        "http://localhost:8080/realms/hoplife-realm/protocol/openid-connect/logout"
        "?client_id=hoplife-backend"
        "&post_logout_redirect_uri=http://localhost:8000/"
    )

    return render(request, "usuarios/logout.html", {"keycloak_logout_url": keycloak_logout_url})
