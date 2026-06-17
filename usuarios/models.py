from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="perfil"
    )
    keycloak_id = models.CharField(
        max_length=255, unique=True, null=True, blank=True, db_index=True
    )
    data_nascimento = models.DateField(null=True, blank=True)
    
    # CAMPOS PARA ACESSIBILIDADE
    tamanho_texto = models.CharField(
        max_length=15, 
        default='medio', 
        choices=[('pequeno', 'Pequeno'), ('medio', 'Médio'), ('grande', 'Grande')]
    )
    tamanho_botao = models.CharField(
        max_length=15, 
        default='normal', 
        choices=[('normal', 'Normal'), ('largo', 'Largo')]
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} ({self.keycloak_id})"

    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuários"