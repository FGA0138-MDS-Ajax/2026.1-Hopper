from django.contrib import admin

from .models import Categoria, Meta, RegistroDiario

# Apenas registra a Categoria normalmente
admin.site.register(Categoria)


@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    # Quais colunas vão aparecer na tabela do painel
    list_display = ("titulo", "usuario", "categoria", "data_criacao")

    # Cria um menu lateral direito para filtrar os dados
    list_filter = ("usuario", "categoria")

    # Adiciona uma barra de pesquisa no topo (busca por título ou nome do usuário)
    search_fields = ("titulo", "usuario__username", "usuario__first_name")


@admin.register(RegistroDiario)
class RegistroDiarioAdmin(admin.ModelAdmin):
    # Mostra os detalhes certinhos de cada quadradinho salvo
    list_display = ("meta", "get_usuario", "data", "status_conclusao")
    list_filter = ("status_conclusao", "data", "meta__usuario")

    # Função para puxar o nome do usuário através da Meta
    def get_usuario(self, obj):
        return obj.meta.usuario

    get_usuario.short_description = "Usuário"  # Nome da coluna
