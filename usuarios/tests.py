from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase

from .models import PerfilUsuario


class AutenticacaoIntegracaoTest(TestCase):
    @patch("usuarios.services.keycloak_openid.token")
    @patch("usuarios.services.keycloak_openid.userinfo")
    def test_ct01_registro_e_login_com_redirecionamento(
        self, mock_userinfo, mock_token
    ):
        """CT-01: Simula o retorno do Keycloak, garante a criação do usuário no banco
        e verifica o redirecionamento para a página inicial."""

        mock_token.return_value = {"access_token": "token_testes"}

        mock_userinfo.return_value = {
            "sub": "abc-123-codigo-unico",
            "preferred_username": "usuario.teste",
            "email": "teste@hoplife.com",
            "given_name": "Usuário",
        }

        response = self.client.get("/usuarios/callback/?code=token_falso_de_teste")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login realizado com sucesso!")
        self.assertContains(response, "Olá, Usuário")

        usuario_criado = User.objects.filter(username="usuario.teste").first()
        self.assertIsNotNone(usuario_criado, "O User nativo não foi criado.")

        perfil_criado = PerfilUsuario.objects.filter(
            keycloak_id="abc-123-codigo-unico"
        ).first()
        self.assertIsNotNone(perfil_criado, "O PerfilUsuario não foi criado.")
        self.assertEqual(perfil_criado.usuario, usuario_criado)
