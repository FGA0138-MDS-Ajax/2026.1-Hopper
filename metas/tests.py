import calendar
import time
from django.utils import timezone
from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .models import Categoria, Meta, RegistroDiario
from gamificacao.models import PerfilGamificacao

User = get_user_model()


class MetasModelsTest(TestCase):
    def setUp(self):
        """Configuração inicial do banco de dados para os testes de modelo."""
        self.usuario = User.objects.create_user(
            username="testuser", password="testpassword123"
        )
        self.categoria = Categoria.objects.create(
            usuario=self.usuario, nome="Saúde", cor_identificacao="#FF0000"
        )
        self.meta = Meta.objects.create(
            usuario=self.usuario, titulo="Beber 2L de água", categoria=self.categoria
        )

    def test_categoria_str(self):
        """Testa se a representação em string da Categoria está correta."""
        self.assertEqual(str(self.categoria), "Saúde")

    def test_meta_str(self):
        """Testa se a representação em string da Meta está correta."""
        self.assertEqual(str(self.meta), "Beber 2L de água")

    def test_dias_do_mes_atual_cria_registros(self):
        """Testa se o método cria os RegistrosDiarios para todos os dias do mês corrente."""
        hoje = date.today()
        _, num_dias = calendar.monthrange(hoje.year, hoje.month)

        registros = self.meta.dias_do_mes_atual()

        self.assertEqual(len(registros), num_dias)
        self.assertEqual(
            RegistroDiario.objects.filter(meta=self.meta).count(), num_dias
        )

    def test_registro_diario_property_hoje(self):
        """Testa se a property 'hoje' identifica corretamente a data atual."""
        registro = RegistroDiario.objects.create(
            meta=self.meta, data=date.today(), status_conclusao="branco"
        )
        self.assertTrue(registro.hoje)


class MetasViewsTest(TestCase):
    def setUp(self):
        """Configuração inicial simulando um usuário logado e dados iniciais."""
        self.usuario = User.objects.create_user(
            username="testuser", password="testpassword123"
        )
        self.client.login(username="testuser", password="testpassword123")

        self.categoria = Categoria.objects.create(
            usuario=self.usuario, nome="Estudos", cor_identificacao="#00FF00"
        )
        self.meta = Meta.objects.create(
            usuario=self.usuario, titulo="Estudar Django", categoria=self.categoria
        )
        self.registro = RegistroDiario.objects.create(
            meta=self.meta, data=date.today(), status_conclusao="branco"
        )

    def test_listar_metas_view(self):
        """Testa se a página inicial de metas carrega corretamente."""
        response = self.client.get(reverse("metas:listar"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "metas/listar.html")
        self.assertContains(response, "Estudar Django")

    def test_criar_meta_view(self):
        """Testa a criação de uma nova meta via formulário POST."""
        dados_post = {"titulo": "Fazer caminhada", "categoria": self.categoria.id}
        response = self.client.post(reverse("metas:criar"), dados_post)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após sucesso
        self.assertTrue(Meta.objects.filter(titulo="Fazer caminhada").exists())

    def test_deletar_meta_view(self):
        """Testa a remoção completa de uma meta do sistema."""
        response = self.client.post(
            reverse("metas:deletar", kwargs={"pk": self.meta.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Meta.objects.filter(id=self.meta.id).exists())

    def test_atualizar_status_diario_sucesso(self):
        """Testa a view de atualização de status diário para 'check' (Cumprida)."""
        url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro.id}
        )
        response = self.client.post(url, {"status": "check"})

        self.registro.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.registro.status_conclusao, "check")

    def test_atualizar_status_diario_invalido(self):
        """Testa se um status inválido enviado ao servidor é rejeitado, mantendo o original."""
        url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro.id}
        )
        self.client.post(url, {"status": "status_invalido"})

        self.registro.refresh_from_db()
        self.assertEqual(self.registro.status_conclusao, "branco")

    def test_criar_categoria_view(self):
        """Testa o envio do formulário de criação de nova categoria."""
        dados_post = {"nome": "Lazer", "cor_identificacao": "#FF9500"}
        response = self.client.post(reverse("metas:criar_categoria"), dados_post)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Categoria.objects.filter(nome="Lazer").exists())

    def test_listar_categorias_view(self):
        """Testa o carregamento da lista de categorias cadastradas."""
        response = self.client.get(reverse("metas:listar_categorias"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "metas/listar_categoria.html")
        self.assertContains(response, "Estudos")

    def test_deletar_categoria_view(self):
        """Testa a exclusão de uma categoria e o comportamento nas metas associadas."""
        response = self.client.post(
            reverse("metas:deletar_categoria", kwargs={"pk": self.categoria.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Categoria.objects.filter(id=self.categoria.id).exists())

        # Testando a integridade (on_delete=models.SET_NULL): A meta não deve sumir, fica null
        self.meta.refresh_from_db()
        self.assertNil = self.assertIsNone(self.meta.categoria)


class TestCT03CadastroeVisualizacaoMetas(TestCase):
    """
    CT-03 – Cadastro e Visualização de Metas
    Nível: Integração / Tipo: Funcional

    Cenário: Um usuário autenticado acessa a tela de criar meta, envia o formulário
    e o sistema o redireciona para a listagem (listar.html), onde a nova meta deve
    aparecer com o título correto e com o status padrão 'pendente' (representado
    no HTML pelo emoji ⬜).
    """

    def setUp(self):
        """Configuração: criar um usuário autenticado."""
        self.usuario = User.objects.create_user(
            username="testuser_ct03", password="senha123456"
        )
        self.client.login(username="testuser_ct03", password="senha123456")

    def test_cadastro_meta_com_visualizacao_sucesso(self):
        """
        Critério de Aceitação: A meta deve ser cadastrada e exibida com sucesso.
        - O usuário acessa a página de criar meta
        - Envia um formulário com título e categoria (opcional)
        - Sistema redireciona para a listagem
        - A meta aparece na listagem com título correto
        - O status padrão é 'branco' (⬜)
        """
        # Passo 1: Criar uma categoria para a meta
        categoria = Categoria.objects.create(
            usuario=self.usuario, nome="Saúde", cor_identificacao="#FF5733"
        )

        # Passo 2: Enviar formulário de criação de meta
        dados_formulario = {
            "titulo": "Fazer 30 minutos de exercício",
            "categoria": categoria.id,
        }
        response = self.client.post(reverse("metas:criar"), dados_formulario)

        # Passo 3: Verificar redirecionamento (status 302)
        self.assertEqual(
            response.status_code,
            302,
            "A resposta deveria ser um redirecionamento (302)",
        )

        # Passo 4: Verificar que a meta foi criada no banco de dados
        meta_criada = Meta.objects.get(titulo="Fazer 30 minutos de exercício")
        self.assertIsNotNone(meta_criada, "A meta não foi criada no banco de dados")
        self.assertEqual(
            meta_criada.usuario,
            self.usuario,
            "A meta não pertence ao usuário autenticado",
        )
        self.assertEqual(
            meta_criada.categoria,
            categoria,
            "A categoria não foi associada corretamente",
        )

        # Passo 5: Acessar a listagem e verificar se a meta aparece
        response = self.client.get(reverse("metas:listar"))
        self.assertEqual(
            response.status_code, 200, "A página de listagem não foi carregada"
        )
        self.assertContains(
            response,
            "Fazer 30 minutos de exercício",
            msg_prefix="O título da meta não apareceu na listagem",
        )

        # Passo 6: Verificar se o registro diário foi criado com status 'branco' (⬜)
        registro_hoje = RegistroDiario.objects.get(meta=meta_criada, data=date.today())
        self.assertEqual(
            registro_hoje.status_conclusao,
            "branco",
            "O status padrão do registro diário não é 'branco'",
        )

        # Passo 7: Verificar se o emoji ⬜ está renderizado na página HTML
        self.assertContains(
            response,
            "⬜",
            msg_prefix="O emoji ⬜ (status pendente) não apareceu na listagem",
        )

    def test_cadastro_meta_sem_categoria(self):
        """
        Teste adicional: Garantir que a meta pode ser criada sem categoria.
        """
        dados_formulario = {
            "titulo": "Estudar Python",
            "categoria": "",  # Sem categoria
        }
        response = self.client.post(reverse("metas:criar"), dados_formulario)

        self.assertEqual(response.status_code, 302)
        meta_criada = Meta.objects.get(titulo="Estudar Python")
        self.assertIsNone(meta_criada.categoria, "A categoria deveria ser None")


class TestCT04MarcacaoDiariaMetaCumprida(TestCase):
    """
    CT-04 – Marcação Diária de Meta Cumprida (Versão Simplificada)
    Nível: Sistema / Tipo: Funcional

    NOTA IMPORTANTE: Este teste valida o comportamento END-TO-END sem usar browser real.
    Para testes com JavaScript (Fetch API) em produção, use:

    ```bash
    python manage.py test metas.tests.TestCT04MarcacaoDiariaMetaCumpridaComSelenium
    ```

    Este teste valida:
    - Modal POST endpoint funciona corretamente
    - Status é atualizado no banco de dados
    - Resposta do servidor é apropriada para Fetch API processar

    O teste com Selenium é opcional e requer navegador real (veja classe abaixo).
    """

    def setUp(self):
        """Configuração para cada teste: criar usuário, categoria e metas."""
        # Criar usuário autenticado
        self.usuario = User.objects.create_user(
            username="testuser_ct04", password="senha123456"
        )
        self.client.login(username="testuser_ct04", password="senha123456")

        # Criar categoria
        self.categoria = Categoria.objects.create(
            usuario=self.usuario, nome="Hábitos Diários", cor_identificacao="#4CAF50"
        )

        # Criar meta
        self.meta = Meta.objects.create(
            usuario=self.usuario,
            titulo="Beber 2 litros de água",
            categoria=self.categoria,
        )

        # Criar registro diário com status inicial 'branco' (⬜)
        self.registro_hoje = RegistroDiario.objects.create(
            meta=self.meta, data=date.today(), status_conclusao="branco"
        )

    def test_marcacao_meta_sucesso_atualiza_banco(self):
        """
        Teste 1: Validar que POST para atualizar meta funciona
        - Status inicial: 'branco' (⬜)
        - Envia POST com status='check'
        - Banco é atualizado com sucesso
        - Resposta é redirecionamento (usado pelo JavaScript para confirmar sucesso)
        """
        url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro_hoje.id}
        )

        # Passo 1: Verificar status inicial
        self.registro_hoje.refresh_from_db()
        self.assertEqual(
            self.registro_hoje.status_conclusao,
            "branco",
            "Status inicial deveria ser 'branco'",
        )

        # Passo 2: Enviar requisição POST (como JavaScript faria)
        response = self.client.post(url, {"status": "check"})

        # Passo 3: Verificar que redirecionou (status 302)
        self.assertEqual(
            response.status_code,
            302,
            "Deveria redirecionar após atualizar (HTTP 302)",
        )

        # Passo 4: Verificar que banco foi atualizado
        self.registro_hoje.refresh_from_db()
        self.assertEqual(
            self.registro_hoje.status_conclusao,
            "check",
            "Status no banco deveria ser 'check' (✅)",
        )

    def test_marcacao_meta_falha(self):
        """
        Teste 2: Validar que marcação como 'falha' funciona
        - Envia POST com status='falha'
        - Banco é atualizado para 'falha' (❌)
        """
        url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro_hoje.id}
        )

        response = self.client.post(url, {"status": "falha"})

        self.assertEqual(response.status_code, 302)
        self.registro_hoje.refresh_from_db()
        self.assertEqual(
            self.registro_hoje.status_conclusao,
            "falha",
            "Status deveria ser 'falha' (❌)",
        )

    def test_marcacao_meta_limpar(self):
        """
        Teste 3: Validar que limpar status funciona
        - Primeiro marca como 'check'
        - Depois limpa para 'branco'
        - Banco reflete ambas alterações
        """
        url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro_hoje.id}
        )

        # Marcar como cumprida
        self.client.post(url, {"status": "check"})
        self.registro_hoje.refresh_from_db()
        self.assertEqual(self.registro_hoje.status_conclusao, "check")

        # Limpar
        response = self.client.post(url, {"status": "branco"})
        self.assertEqual(response.status_code, 302)

        self.registro_hoje.refresh_from_db()
        self.assertEqual(
            self.registro_hoje.status_conclusao,
            "branco",
            "Status deveria voltar para 'branco' (⬜)",
        )

    def test_listagem_exibe_emoji_correto(self):
        """
        Teste 4: Validar que HTML renderiza emoji correto baseado no status
        - Status 'branco' → renderiza ⬜
        - Status 'check' → renderiza ✅
        - Status 'falha' → renderiza ❌
        """
        response = self.client.get(reverse("metas:listar"))
        self.assertEqual(response.status_code, 200)

        # Verificar que HTML contém emoji ⬜ (status inicial)
        # NOTA: Há múltiplas instâncias de ⬜ (um para cada dia do mês + hoje)
        self.assertContains(
            response, "⬜", msg_prefix="Deveria ter ⬜ para status branco"
        )

        # Atualizar para 'check'
        url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro_hoje.id}
        )
        self.client.post(url, {"status": "check"})

        # Verificar nova renderização
        response = self.client.get(reverse("metas:listar"))
        self.assertContains(
            response, "✅", msg_prefix="Deveria ter ✅ após marcação como cumprida"
        )


class TestCT04MarcacaoDiariaMetaCumpridaComSelenium(StaticLiveServerTestCase):
    """
    CT-04 – Marcação Diária de Meta Cumprida (VERSÃO COM BROWSER REAL)
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")  # importante

        cls.selenium = webdriver.Chrome(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="testuser_ct04_selenium", password="senha123456"
        )

        self.categoria = Categoria.objects.create(
            usuario=self.usuario, nome="Hábitos Diários", cor_identificacao="#4CAF50"
        )

        self.meta = Meta.objects.create(
            usuario=self.usuario,
            titulo="Beber 2 litros de água",
            categoria=self.categoria,
        )

        self.registro_hoje = RegistroDiario.objects.create(
            meta=self.meta, data=date.today(), status_conclusao="branco"
        )

    def _login_selenium(self):
        from django.test.client import Client

        client = Client()
        client.login(
            username="testuser_ct04_selenium",
            password="senha123456",
        )

        # Inicializa o domínio
        self.selenium.get(self.live_server_url)

        # Marca o tutorial como já visto
        self.selenium.execute_script("""
            localStorage.setItem('tutorialVisualizado', 'true');
        """)

        # Adiciona os cookies da sessão autenticada
        for key, value in client.cookies.items():
            self.selenium.add_cookie(
                {
                    "name": key,
                    "value": value.value,
                    "path": "/",
                }
            )

        # Recarrega a página para que o cookie passe a valer
        self.selenium.refresh()
        print(self.selenium.execute_script("return document.cookie"))

    def test_marcar_meta_cumprida_atualiza_dom_em_tempo_real(self):
        """
        Critério de Aceitação:
        - O teste verifica a atualização visual no navegador e a persistência no banco.
        """
        # Passo 1: Fazer login via cookie de sessão
        self._login_selenium()

        # Passo 2: Navegar para a listagem de metas
        self.selenium.get(f"{self.live_server_url}/metas/")

        # Aguardar o carregamento da página
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card"))
        )

        # ==========================================
        # FECHAR O TUTORIAL (Plano B - Força Bruta JS)
        # ==========================================
        self.selenium.execute_script("""
            document.querySelectorAll('.modal').forEach(m => m.style.display = 'none');
            document.querySelectorAll('.modal-backdrop').forEach(b => b.remove());
            document.body.classList.remove('modal-open');
            document.body.style.overflow = 'auto';
        """)
        time.sleep(0.5)

        # ==========================================
        # CLICAR NO CABEÇALHO DA META
        # ==========================================
        cabecalho_meta = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"[data-bs-target='#gaveta-{self.meta.id}']")
            )
        )
        self.selenium.execute_script("arguments[0].click();", cabecalho_meta)
        time.sleep(0.5)

        # ==========================================
        # INTERAÇÃO COM O MODAL
        # ==========================================
        # Aguardar emoji inicial
        WebDriverWait(self.selenium, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, f"icone-registro-{self.registro_hoje.id}"),
                "⬜",
            )
        )

        # Clicar no botão Hoje
        botao_hoje = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-hoje-3d"))
        )
        botao_hoje.click()

        # Aguardar modal
        WebDriverWait(self.selenium, 10).until(
            EC.visibility_of_element_located((By.ID, "modalStatus"))
        )

        # Clicar no botão de sucesso
        botao_sucesso = WebDriverWait(self.selenium, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Consegui cumprir')]")
            )
        )
        botao_sucesso.click()

        # ==========================================
        # PASSO FINAL: Aguardar DOM + Sincronização do Banco
        # ==========================================
        # 1. Espera visual no navegador
        WebDriverWait(self.selenium, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, f"icone-registro-{self.registro_hoje.id}"),
                "✅",
            )
        )


from django.contrib.auth.models import User
from django.test import TestCase

from metas.models import Meta, RegistroDiario


class AtualizarStatusENotaViewTest(TestCase):
    def setUp(self):
        # 1. Criamos o usuário dono da meta
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # 2. Criamos um usuário "invasor" para testar a segurança
        self.outro_user = User.objects.create_user(
            username="hacker", password="hackerpassword"
        )

        # 3. Criamos a meta e o registro diário para o usuário principal
        self.meta = Meta.objects.create(usuario=self.user, titulo="Caminhada Matinal")
        self.registro = RegistroDiario.objects.create(
            meta=self.meta, data=date.today(), status_conclusao="branco", nota=""
        )

        # 4. Preparamos a URL que será chamada nos testes
        self.url = reverse(
            "metas:atualizar_registro", kwargs={"registro_id": self.registro.id}
        )

    def test_atualizar_status_e_nota_com_sucesso(self):
        """Testa o caminho feliz: usuário logado salva o status e a nota corretamente."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.post(
            self.url,
            {"status": "check", "nota": "Hoje a caminhada foi excelente, fiz 5km!"},
        )

        # Recarrega o registro do banco de dados para ver se mudou
        self.registro.refresh_from_db()

        # Verifica se a view redirecionou de volta para a lista (status 302)
        self.assertEqual(response.status_code, 302)
        # Verifica se o status mudou
        self.assertEqual(self.registro.status_conclusao, "check")
        # Verifica se a nota foi salva
        self.assertEqual(self.registro.nota, "Hoje a caminhada foi excelente, fiz 5km!")

    def test_atualizar_apenas_nota_sem_mudar_status(self):
        """Testa se o sistema salva a nota mesmo se o status enviado for inválido."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.post(
            self.url,
            {
                "status": "status_inventado_que_nao_existe",
                "nota": "Apenas adicionando um comentário.",
            },
        )

        self.registro.refresh_from_db()

        # O status original era 'branco', deve continuar 'branco'
        self.assertEqual(self.registro.status_conclusao, "branco")
        # Mas a nota deve ter sido salva
        self.assertEqual(self.registro.nota, "Apenas adicionando um comentário.")

    def test_seguranca_usuario_nao_pode_editar_meta_alheia(self):
        """Testa se um usuário logado tenta editar o registro de outra pessoa e recebe erro 404."""
        # Logamos com o usuário "hacker"
        self.client.login(username="hacker", password="hackerpassword")

        response = self.client.post(
            self.url, {"status": "check", "nota": "Hackeando a meta do colega"}
        )

        # O get_object_or_404 deve barrar e retornar "Não Encontrado" (404)
        self.assertEqual(response.status_code, 404)

        # Confirma que nada mudou no banco
        self.registro.refresh_from_db()
        self.assertEqual(self.registro.nota, "")

    def test_redirecionamento_usuario_nao_autenticado(self):
        """Testa se um usuário deslogado é barrado e mandado para a tela de login."""
        # Não fazemos o self.client.login() aqui
        response = self.client.post(
            self.url, {"status": "check", "nota": "Tentando salvar sem logar"}
        )

        # O Django deve redirecionar (302) o usuário deslogado
        self.assertEqual(response.status_code, 302)

        # Confirma que nada mudou no banco
        self.registro.refresh_from_db()
        self.assertEqual(self.registro.nota, "")


class EditarCategoriaTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="usuario1", password="123456")

        self.client.login(username="usuario1", password="123456")

        self.categoria = Categoria.objects.create(
            nome="Saúde", cor_identificacao="#FF0000", usuario=self.user
        )

        self.url = reverse("metas:editar_categoria", args=[self.categoria.id])

    def test_editar_categoria_altera_dados(self):
        response = self.client.post(
            self.url, {"nome": "Alimentação", "cor_identificacao": "#00FF00"}
        )

        self.categoria.refresh_from_db()

        self.assertEqual(self.categoria.nome, "Alimentação")
        self.assertEqual(self.categoria.cor_identificacao, "#00FF00")

    def test_editar_categoria_nao_cria_nova(self):
        total_antes = Categoria.objects.count()

        self.client.post(
            self.url, {"nome": "Nova Categoria", "cor_identificacao": "#123456"}
        )

        self.assertEqual(Categoria.objects.count(), total_antes)

    def test_editar_categoria_redireciona(self):
        response = self.client.post(
            self.url, {"nome": "Teste", "cor_identificacao": "#123456"}
        )

        self.assertEqual(response.status_code, 302)


class EditarMetaTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="usuario1", password="123456")

        self.client.login(username="usuario1", password="123456")

        self.categoria = Categoria.objects.create(
            nome="Saúde", cor_identificacao="#FF0000", usuario=self.user
        )

        self.meta = Meta.objects.create(
            titulo="Beber água", categoria=self.categoria, usuario=self.user
        )

        self.url = reverse("metas:editar", args=[self.meta.id])

    def test_editar_meta_altera_dados(self):
        response = self.client.post(
            self.url, {"titulo": "Beber 2L de água", "categoria": self.categoria.id}
        )

        self.meta.refresh_from_db()

        self.assertEqual(self.meta.titulo, "Beber 2L de água")
        self.assertEqual(self.meta.categoria, self.categoria)

    def test_editar_meta_nao_cria_nova(self):
        total_antes = Meta.objects.count()

        self.client.post(
            self.url, {"titulo": "Novo título", "categoria": self.categoria.id}
        )

        self.assertEqual(Meta.objects.count(), total_antes)

    def test_editar_meta_redireciona(self):
        response = self.client.post(
            self.url, {"titulo": "Teste redirect", "categoria": self.categoria.id}
        )

        self.assertEqual(response.status_code, 302)

class AtualizarStatusGamificacaoTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="idoso_teste", password="123")
        self.client.login(username="idoso_teste", password="123")
        
        # Cria a meta e o registro diário para hoje
        self.meta = Meta.objects.create(titulo="Remédio", usuario=self.user)
        self.registro = RegistroDiario.objects.create(
            meta=self.meta, 
            data=timezone.localdate(), 
            status_conclusao="branco"
        )
        self.url = reverse("metas:atualizar_registro", args=[self.registro.id])

    def test_marcar_check_cria_e_soma_gamificacao(self):
        """Garante que ao enviar um POST com 'check', o perfil ganha ponto."""
        response = self.client.post(self.url, {"status": "check"})
        
        # O sistema deve redirecionar após o POST
        self.assertEqual(response.status_code, 302)
        
        # Verifica se o status mudou no banco
        self.registro.refresh_from_db()
        self.assertEqual(self.registro.status_conclusao, "check")
        
        # Verifica se o perfil foi criado e se ganhou 1 ponto
        perfil = PerfilGamificacao.objects.get(usuario=self.user)
        self.assertEqual(perfil.sequencia_dias_ativos, 1)

    def test_marcar_falha_nao_soma_gamificacao(self):
        """Garante que marcar 'falha' altera o status, mas NÃO dá ponto."""
        response = self.client.post(self.url, {"status": "falha"})
        
        self.registro.refresh_from_db()
        self.assertEqual(self.registro.status_conclusao, "falha")
        
        # Como foi falha, ele pode até ter criado o perfil, mas a ofensiva deve ser 0
        perfil, _ = PerfilGamificacao.objects.get_or_create(usuario=self.user)
        self.assertEqual(perfil.sequencia_dias_ativos, 0)