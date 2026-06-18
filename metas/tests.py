import calendar
from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Categoria, Meta, RegistroDiario

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
