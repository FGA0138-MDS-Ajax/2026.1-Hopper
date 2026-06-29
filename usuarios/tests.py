import time
from unittest.mock import patch

from django.contrib.auth.models import AnonymousUser, User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import RequestFactory, TestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from usuarios.models import PerfilUsuario

from .context_processors import configuracoes_acessibilidade


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


class AcessibilidadeViewTest(TestCase):
    def setUp(self):
        """Prepara o terreno: cria um usuário e um perfil padrão para ele."""
        self.user = User.objects.create_user(
            username="idoso.teste", password="senha123"
        )
        self.perfil = PerfilUsuario.objects.create(
            usuario=self.user, tamanho_texto="medio", tamanho_botao="normal"
        )
        self.url = reverse("usuarios:acessibilidade")

    def test_acesso_bloqueado_para_usuario_anonimo(self):
        """Garante que a view redireciona para login se o usuário não estiver autenticado."""
        response = self.client.get(self.url)
        # O Django redireciona (302) usuários não logados que tentam acessar rotas com @login_required
        self.assertEqual(response.status_code, 302)

    def test_carregamento_da_pagina_para_usuario_logado(self):
        """Garante que a página carrega perfeitamente (HTTP 200) com o contexto atual do banco."""
        self.client.login(username="idoso.teste", password="senha123")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "usuarios/acessibilidade.html")
        # Verifica se o contexto enviado para o HTML corresponde ao perfil
        self.assertEqual(response.context["tamanho_texto"], "medio")
        self.assertEqual(response.context["tamanho_botao"], "normal")

    def test_atualizar_preferencias_com_sucesso(self):
        """Testa o envio do formulário (POST) e se os dados são salvos no banco de dados."""
        self.client.login(username="idoso.teste", password="senha123")

        # O seu HTML/View espera 'tamanho_letra' e 'tamanho_botao'
        dados_formulario = {"tamanho_letra": "grande", "tamanho_botao": "largo"}

        response = self.client.post(self.url, dados_formulario)

        # Verifica se recarregou a página após salvar (redirect)
        self.assertRedirects(response, self.url)

        # Puxa os dados atualizados do banco para conferir
        self.perfil.refresh_from_db()
        self.assertEqual(self.perfil.tamanho_texto, "grande")
        self.assertEqual(self.perfil.tamanho_botao, "largo")

    def test_ignorar_dados_invalidos_no_formulario(self):
        """Testa a sua validação básica de segurança contra injeção de valores incorretos."""
        self.client.login(username="idoso.teste", password="senha123")

        # Enviando dados que não existem nas suas listas de choices
        dados_hack = {"tamanho_letra": "gigante", "tamanho_botao": "minusculo"}

        self.client.post(self.url, dados_hack)

        self.perfil.refresh_from_db()
        # Os valores devem permanecer intactos como foram criados no setUp
        self.assertEqual(self.perfil.tamanho_texto, "medio")
        self.assertEqual(self.perfil.tamanho_botao, "normal")


class ContextProcessorTest(TestCase):
    def setUp(self):
        # O RequestFactory cria requisições web simuladas sem precisar carregar views
        self.factory = RequestFactory()

        self.user = User.objects.create_user(
            username="idoso.teste", password="senha123"
        )
        self.perfil = PerfilUsuario.objects.create(
            usuario=self.user, tamanho_texto="grande", tamanho_botao="largo"
        )

    def test_contexto_usuario_anonimo(self):
        """Garante que visitantes sem login recebem os tamanhos padrão."""
        request = self.factory.get("/")
        request.user = AnonymousUser()  # Simula alguém que não está logado

        contexto = configuracoes_acessibilidade(request)

        self.assertEqual(contexto["global_tamanho_texto"], "medio")
        self.assertEqual(contexto["global_tamanho_botao"], "normal")

    def test_contexto_usuario_autenticado_com_perfil(self):
        """Garante que usuários logados recebem as configurações salvas no banco."""
        request = self.factory.get("/")
        request.user = self.user  # Associa o nosso usuário de teste à requisição

        contexto = configuracoes_acessibilidade(request)

        self.assertEqual(contexto["global_tamanho_texto"], "grande")
        self.assertEqual(contexto["global_tamanho_botao"], "largo")

    def test_contexto_usuario_sem_perfil(self):
        """Garante o fallback (valores padrão) se ocorrer um erro e o usuário não tiver perfil."""
        user_sem_perfil = User.objects.create_user(username="bugado", password="123")

        request = self.factory.get("/")
        request.user = user_sem_perfil

        contexto = configuracoes_acessibilidade(request)

        self.assertEqual(contexto["global_tamanho_texto"], "medio")
        self.assertEqual(contexto["global_tamanho_botao"], "normal")


class TestCTAcessibilidadeSistema(StaticLiveServerTestCase):
    """
    CT - Alteração das configurações de acessibilidade.
    O teste verifica o fluxo completo pelo navegador.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(
            username="idoso",
            password="senha123",
        )

        self.perfil = PerfilUsuario.objects.create(
            usuario=self.user,
            tamanho_texto="medio",
            tamanho_botao="normal",
        )

    def _login(self):
        from django.test.client import Client

        client = Client()
        client.login(
            username="idoso",
            password="senha123",
        )

        # Inicializa domínio
        self.selenium.get(self.live_server_url)

        # Não mostrar tutorial
        self.selenium.execute_script("""
            localStorage.setItem('tutorialVisualizado', 'true');
        """)

        # Copia cookies da sessão
        for key, value in client.cookies.items():
            self.selenium.add_cookie(
                {
                    "name": key,
                    "value": value.value,
                    "path": "/",
                }
            )

        self.selenium.refresh()

    def test_alterar_configuracoes_acessibilidade(self):

        # Login
        self._login()

        # Abre a página
        self.selenium.get(f"{self.live_server_url}/usuarios/acessibilidade/")

        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "letra_grande"))
        )

        # Fecha qualquer modal do tutorial
        self.selenium.execute_script("""
            document.querySelectorAll('.modal').forEach(m => m.style.display='none');
            document.querySelectorAll('.modal-backdrop').forEach(b => b.remove());
            document.body.classList.remove('modal-open');
            document.body.style.overflow='auto';
        """)

        # Seleciona "Grande"
        self.selenium.find_element(By.CSS_SELECTOR, "label[for='letra_grande']").click()

        # Seleciona "Botões Grandes"
        self.selenium.find_element(By.CSS_SELECTOR, "label[for='botao_grande']").click()

        # Salva
        botao_salvar = self.selenium.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )

        # Garante que o botão está visível
        self.selenium.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            botao_salvar,
        )

        time.sleep(0.5)

        # Clica via JavaScript
        self.selenium.execute_script(
            "arguments[0].click();",
            botao_salvar,
        )

        # Espera voltar para a própria página
        WebDriverWait(self.selenium, 10).until(
            EC.url_contains("/usuarios/acessibilidade/")
        )

        # Confere o banco
        self.perfil.refresh_from_db()

        self.assertEqual(self.perfil.tamanho_texto, "grande")

        self.assertEqual(self.perfil.tamanho_botao, "largo")

        # Reabre a página
        self.selenium.get(f"{self.live_server_url}/usuarios/acessibilidade/")

        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "letra_grande"))
        )

        # Confere que continuam marcados
        self.assertTrue(self.selenium.find_element(By.ID, "letra_grande").is_selected())

        self.assertTrue(self.selenium.find_element(By.ID, "botao_grande").is_selected())
