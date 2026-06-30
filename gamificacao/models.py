from datetime import timedelta
from django.conf import settings
from django.db import models
from django.utils import timezone


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

    def verificar_quebra_de_ofensiva(self):
        """
        Verifica se o usuário ficou mais de 1 dia sem interagir.
        Se sim, a ofensiva atual é zerada.
        """
        hoje = timezone.localdate()
        
        # Se ele tem uma última interação e ela foi antes de ontem, ele quebrou o streak
        if self.ultima_interacao and self.ultima_interacao < hoje - timedelta(days=1):
            self.sequencia_dias_ativos = 0
            self.save()

    def registrar_check_in(self):
        """
        Chamado toda vez que o idoso marca uma meta como "Cumprida".
        Faz a matemática de somar dias e atualizar recordes.
        """
        hoje = timezone.localdate()

        # Primeiro, verifica se o streak antigo já morreu
        self.verificar_quebra_de_ofensiva()

        if self.ultima_interacao != hoje:
            # Se a última interação não foi hoje, significa que é o primeiro check do dia
            self.sequencia_dias_ativos += 1
            self.ultima_interacao = hoje

            # Verifica se bateu um novo recorde pessoal
            if self.sequencia_dias_ativos > self.maior_sequencia_historica:
                self.maior_sequencia_historica = self.sequencia_dias_ativos

            self.save()