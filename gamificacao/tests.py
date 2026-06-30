from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Ajuste os imports abaixo caso o caminho das suas models seja ligeiramente diferente
from metas.models import Meta, RegistroDiario
from gamificacao.models import PerfilGamificacao


class EstatisticasViewTest(TestCase):
    def setUp(self):
        # 1. Preparação do Usuário e Login
        self.user = User.objects.create_user(
            username="testuser", password="password123", first_name="Jogador"
        )
        self.client.login(username="testuser", password="password123")
        self.url = reverse("gamificacao:estatisticas")

        # 2. Preparação da Meta
        self.meta = Meta.objects.create(titulo="Beber Água", usuario=self.user)

        # 3. Gerenciamento de Datas Relativas (para o teste nunca quebrar com o passar do tempo)
        self.hoje = timezone.localdate()
        self.ontem = self.hoje - timedelta(days=1)
        self.cinco_dias_atras = self.hoje - timedelta(days=5)
        self.ano_passado = self.hoje - timedelta(days=366)

        # 4. Criação dos Registros
        # Registro de Hoje (Entra em Semana, Mês, Ano e Geral)
        RegistroDiario.objects.create(meta=self.meta, data=self.hoje, status_conclusao="check")
        
        # Registro de Ontem (Entra em Semana, Mês, Ano e Geral)
        RegistroDiario.objects.create(meta=self.meta, data=self.ontem, status_conclusao="falha")
        
        # Registro de 5 dias atrás (Entra em Semana, Mês, Ano e Geral)
        RegistroDiario.objects.create(meta=self.meta, data=self.cinco_dias_atras, status_conclusao="branco")
        
        # Registro do Ano Passado (Entra APENAS em Geral)
        RegistroDiario.objects.create(meta=self.meta, data=self.ano_passado, status_conclusao="check")

        # 5. Preparação do Perfil de Gamificação (Ofensivas)
        self.perfil = PerfilGamificacao.objects.create(
            usuario=self.user,
            sequencia_dias_ativos=7,
            maior_sequencia_historica=21
        )

    def test_acesso_bloqueado_para_usuario_anonimo(self):
        """Garante que a view proteja os dados de quem não tem login."""
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirecionamento de login_required

    def test_contexto_periodo_geral_e_ofensivas(self):
        """Testa se o filtro 'geral' puxa absolutamente todos os registros e se os streaks carregam."""
        response = self.client.get(self.url)  # Sem GET params, o padrão é 'geral'
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gamificacao/estatisticas.html")
        
        contexto = response.context
        self.assertEqual(contexto["periodo"], "geral")
        self.assertEqual(contexto["total_registros"], 4)
        self.assertEqual(contexto["total_check"], 2)   # Hoje e Ano Passado
        self.assertEqual(contexto["total_falha"], 1)   # Ontem
        self.assertEqual(contexto["total_branco"], 1)  # 5 dias atrás
        
        # Confere se os streaks foram pro contexto corretamente
        self.assertEqual(contexto["ofensiva"], 7)
        self.assertEqual(contexto["recorde"], 21)

    def test_contexto_filtro_semana(self):
        """Testa se o filtro 'semana' ignora dados mais antigos que 6 dias."""
        response = self.client.get(self.url, {"periodo": "semana"})
        
        contexto = response.context
        self.assertEqual(contexto["periodo"], "semana")
        
        # Deve encontrar Hoje, Ontem e 5 dias atrás. Ignora o Ano Passado.
        self.assertEqual(contexto["total_registros"], 3)
        self.assertEqual(contexto["total_check"], 1)  # Apenas o de Hoje entra na conta

    def test_contexto_filtro_ano(self):
        """Testa se o filtro 'ano' pega apenas os registros do ano corrente."""
        response = self.client.get(self.url, {"periodo": "ano"})
        
        contexto = response.context
        self.assertEqual(contexto["periodo"], "ano")
        
        # Deve ignorar o registro de 366 dias atrás, sobrando apenas 3 registros
        self.assertEqual(contexto["total_registros"], 3)

    def test_criacao_automatica_de_perfil_gamificacao(self):
        """Garante que se um usuário não tiver perfil de gamificação, a view cria na hora (get_or_create)."""
        # Criamos um usuário zerado, sem o PerfilGamificacao atrelado
        user_novo = User.objects.create_user(username="novato", password="123")
        self.client.login(username="novato", password="123")
        
        response = self.client.get(self.url)
        
        # A view deve ter executado o get_or_create com sucesso
        self.assertEqual(response.context["ofensiva"], 0)
        self.assertEqual(response.context["recorde"], 0)
        self.assertTrue(PerfilGamificacao.objects.filter(usuario=user_novo).exists())


class PerfilGamificacaoModelTest(TestCase):
    def test_str_do_modelo(self):
        """Garante que a representação em texto do modelo no Admin (ou terminal) está correta."""
        user = User.objects.create_user(username="marcos", first_name="Marcos")
        perfil = PerfilGamificacao.objects.create(usuario=user)
        
        self.assertEqual(str(perfil), "Ofensiva de Marcos")

class PerfilGamificacaoLogicaTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="jogador2", password="123")
        self.perfil = PerfilGamificacao.objects.create(usuario=self.user)
        self.hoje = timezone.localdate()

    def test_registrar_primeiro_checkin(self):
        """Testa se o primeiro check-in do dia soma 1 ponto e atualiza a data."""
        self.perfil.registrar_check_in()
        
        self.perfil.refresh_from_db()
        self.assertEqual(self.perfil.sequencia_dias_ativos, 1)
        self.assertEqual(self.perfil.maior_sequencia_historica, 1)
        self.assertEqual(self.perfil.ultima_interacao, self.hoje)

    def test_apenas_um_ponto_por_dia(self):
        """Garante que clicar em 5 metas no mesmo dia só dá 1 ponto de ofensiva."""
        # Finge que o usuário clicou 3 vezes hoje
        self.perfil.registrar_check_in()
        self.perfil.registrar_check_in()
        self.perfil.registrar_check_in()
        
        self.perfil.refresh_from_db()
        # A ofensiva deve continuar sendo 1
        self.assertEqual(self.perfil.sequencia_dias_ativos, 1)

    def test_manter_ofensiva_dia_seguinte(self):
        """Se ele fez ontem e fez hoje, a ofensiva deve ir para 2."""
        # Finge que a última vez foi ontem e ele já tinha 1 ponto
        self.perfil.ultima_interacao = self.hoje - timedelta(days=1)
        self.perfil.sequencia_dias_ativos = 1
        self.perfil.save()

        # Faz o check-in de hoje
        self.perfil.registrar_check_in()
        
        self.perfil.refresh_from_db()
        self.assertEqual(self.perfil.sequencia_dias_ativos, 2)
        self.assertEqual(self.perfil.maior_sequencia_historica, 2)

    def test_quebra_de_ofensiva(self):
        """Se ele ficou 2 dias sem entrar, a ofensiva deve zerar antes de somar."""
        # Finge que a última interação foi há 2 dias atrás, e ele tinha 50 pontos
        self.perfil.ultima_interacao = self.hoje - timedelta(days=2)
        self.perfil.sequencia_dias_ativos = 50
        self.perfil.maior_sequencia_historica = 50
        self.perfil.save()

        # Faz o check-in hoje
        self.perfil.registrar_check_in()
        
        self.perfil.refresh_from_db()
        # A ofensiva zerou e depois somou o ponto de hoje, logo = 1
        self.assertEqual(self.perfil.sequencia_dias_ativos, 1)
        # Mas o recorde histórico de 50 tem que continuar intacto!
        self.assertEqual(self.perfil.maior_sequencia_historica, 50)