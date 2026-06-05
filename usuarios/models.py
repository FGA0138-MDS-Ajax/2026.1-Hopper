# usuarios/models.py
from django.contrib.auth.models import User
from django.db import models


class PerfilUsuario(models.Model):
    TEXT_SIZE_CHOICES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]
    BUTTON_SIZE_CHOICES = [
        ('normal', 'Normal'),
        ('largo', 'Largo'),
    ]

    # Ligação com o User do Django (usado no views.py atual)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil"
    )

    # ID do Keycloak para identificar o usuário externamente
    keycloak_id = models.CharField(
        max_length=255, unique=True, null=True, blank=True, db_index=True
    )

    data_nascimento = models.DateField(null=True, blank=True)

    # --- CAMPOS DE ACESSIBILIDADE ---
    tamanho_texto = models.CharField(
        max_length=10,
        choices=TEXT_SIZE_CHOICES,
        default='medio',
        verbose_name="Tamanho do Texto"
    )
    tamanho_botao = models.CharField(
        max_length=10,
        choices=BUTTON_SIZE_CHOICES,
        default='normal',
        verbose_name="Tamanho dos Botões"
    )
    assistencia_motora_ativa = models.BooleanField(
        default=False,
        verbose_name="Ativar Assistência Motora"
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} ({self.keycloak_id})"

    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuários"
