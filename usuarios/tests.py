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

        self.assertRedirects(response, "/", target_status_code=200)

        usuario_criado = User.objects.filter(username="usuario.teste").first()
        self.assertIsNotNone(usuario_criado, "O User nativo não foi criado.")

        perfil_criado = PerfilUsuario.objects.filter(
            keycloak_id="abc-123-codigo-unico"
        ).first()
        self.assertIsNotNone(perfil_criado, "O PerfilUsuario não foi criado.")
        self.assertEqual(perfil_criado.usuario, usuario_criado)


class AcessibilidadeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="usuario.acessibilidade", password="password123")
        self.perfil = PerfilUsuario.objects.create(usuario=self.user)

    def test_acessibilidade_view_requires_login(self):
        response = self.client.get("/usuarios/acessibilidade/")
        # Django login_required redirects to login page with next parameter
        self.assertEqual(response.status_code, 302)

    def test_acessibilidade_view_loads_preferences(self):
        self.client.force_login(self.user)
        response = self.client.get("/usuarios/acessibilidade/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value="medio" checked')
        self.assertContains(response, 'value="normal" checked')

    def test_acessibilidade_view_saves_preferences(self):
        self.client.force_login(self.user)
        post_data = {
            "tamanho_letra": "grande",
            "tamanho_botao": "largo",
            "assistencia_motora_ativa": "on"
        }
        response = self.client.post("/usuarios/acessibilidade/", post_data)
        self.assertRedirects(response, "/usuarios/acessibilidade/")

        # Verify database update
        self.perfil.refresh_from_db()
        self.assertEqual(self.perfil.tamanho_texto, "grande")
        self.assertEqual(self.perfil.tamanho_botao, "largo")
        self.assertTrue(self.perfil.assistencia_motora_ativa)

    def test_context_processor_unauthenticated(self):
        # Unauthenticated request should have default context values
        response = self.client.get("/")
        self.assertEqual(response.context.get("tamanho_texto"), "medio")
        self.assertEqual(response.context.get("tamanho_botao"), "normal")
        self.assertFalse(response.context.get("assistencia_motora"))

    def test_context_processor_authenticated(self):
        # Set custom settings first
        self.perfil.tamanho_texto = "pequeno"
        self.perfil.tamanho_botao = "largo"
        self.perfil.assistencia_motora_ativa = True
        self.perfil.save()

        self.client.force_login(self.user)
        response = self.client.get("/")
        self.assertEqual(response.context.get("tamanho_texto"), "pequeno")
        self.assertEqual(response.context.get("tamanho_botao"), "largo")
        self.assertTrue(response.context.get("assistencia_motora"))

