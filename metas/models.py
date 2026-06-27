import calendar
from datetime import date

from django.conf import settings
from django.db import models


class Categoria(models.Model):
    """
    Atende à US6: Categorizar metas em áreas da vida (Saúde, Lazer, etc.)
    """

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    nome = models.CharField(max_length=50)
    # Podemos guardar uma cor em hexadecimal para pintar a interface do idoso depois
    cor_identificacao = models.CharField(max_length=7, default="#007bff")

    def __str__(self):
        return self.nome


class Meta(models.Model):
    """
    A entidade "pai". Representa o objetivo fixo criado pelo idoso.
    """

    # Relaciona a meta ao usuário logado
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=100)

    # Se a categoria for apagada, a meta não some, só fica Sem categoria
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def dias_do_mes_atual(self):
        """
        Retorna os registros de todos os dias do mês atual.
        Cria os dias em branco caso ainda não existam no banco.
        """
        hoje = date.today()
        ano = hoje.year
        mes = hoje.month

        # Descobre quantos dias tem o mês atual
        _, num_dias = calendar.monthrange(ano, mes)

        registros_mes = []

        # Faz um loop do dia 1 até o último dia do mês
        for dia in range(1, num_dias + 1):
            data_alvo = date(ano, mes, dia)

            registro, _ = RegistroDiario.objects.get_or_create(
                meta=self, data=data_alvo
            )
            registros_mes.append(registro)

        return registros_mes


class RegistroDiario(models.Model):
    """
    Relação de composição forte com a Meta.
    É aqui que o GamificacaoService vai calcular os Streaks.
    """

    STATUS_CHOICES = [
        ("check", "Cumprida"),
        ("falha", "Não Cumprida"),
        ("branco", "Neutro"),
    ]

    # related_name='registros' permite buscar todos os dias de uma meta facilmente
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE, related_name="registros")

    data = models.DateField()

    status_conclusao = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="branco"
    )

    nota = models.TextField(
    blank=True,
    null=True,
    verbose_name="Nota do dia"
)

    def __str__(self):
        return (
            f"{self.meta.titulo} - {self.data} - {self.get_status_conclusao_display()}"
        )

    @property
    def hoje(self):
        """Retorna True se este registro for o dia de hoje"""
        return self.data == date.today()
