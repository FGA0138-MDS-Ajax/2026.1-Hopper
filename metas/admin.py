from django.contrib import admin
from .models import Categoria, Meta, RegistroDiario

# 1. Cria o formato "Tabela Embutida" para os Registros Diários
class RegistroDiarioInline(admin.TabularInline):
    model = RegistroDiario
    extra = 0  
    fields = ("data", "status_conclusao")
    ordering = ("-data",) 
    
    # MÁGICA AQUI: Trava a criação manual de novos registros pelo painel Admin
    def has_add_permission(self, request, obj):
        return False


# 2. Configuração da Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "usuario", "cor_identificacao")
    list_filter = ("usuario",)
    search_fields = ("nome", "usuario__username", "usuario__first_name")
    
    readonly_fields = ("usuario",)


# 3. Configuração da Meta
@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario", "categoria", "data_criacao")
    list_filter = ("usuario", "categoria")
    search_fields = ("titulo", "usuario__username", "usuario__first_name", "usuario__email")
    
    readonly_fields = ("usuario",)
    
    # Injeta os registros embutidos dentro da meta
    inlines = [RegistroDiarioInline]

    def get_form(self, request, obj=None, **kwargs):
        form_class = super().get_form(request, obj, **kwargs)
        
        # Filtra as categorias para mostrar apenas as do dono da meta
        if obj and 'categoria' in form_class.base_fields:
            form_class.base_fields['categoria'].queryset = Categoria.objects.filter(usuario=obj.usuario)
            
        return form_class