from django.conf import settings
from django.db import models


class PerfilGamificacao(models.Model):
    """
    Armazena o histórico de engajamento contínuo de um usuário.
    """

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_gamificacao",
    )

    # Contador da ofensiva atual (dias consecutivos cumprindo metas).
    sequencia_dias_ativos = models.PositiveIntegerField(default=0)

    # Troféu de recorde pessoal que guarda a maior ofensiva já alcançada.
    maior_sequencia_historica = models.PositiveIntegerField(default=0)

    # Data do último 'check' para validação da quebra ou soma da ofensiva.
    ultima_interacao = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Retorna a representação em string legível do perfil.
        """
        return f"Ofensiva de {self.usuario.first_name}"
