# Register your models here.
from django.contrib import admin

from .models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    # Mostra essas colunas na tabela principal
    list_display = ("usuario", "keycloak_id")

    # AQUI ESTÁ O SEGREDO: Trava o campo para ninguém fazer besteira!
    readonly_fields = ("keycloak_id", "usuario")
