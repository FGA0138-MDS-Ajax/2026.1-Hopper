from django.contrib import admin
from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import PerfilUsuario
from gamificacao.models import PerfilGamificacao


# 1. Formulário customizado para puxar e salvar a Gamificação dentro do PerfilUsuario
class PerfilUsuarioForm(forms.ModelForm):
    # Criamos os campos soltos para aparecerem na tela
    ofensiva = forms.IntegerField(label="🔥 Ofensiva Atual (Dias)", min_value=0, required=False)
    recorde = forms.IntegerField(label="🏆 Recorde Histórico", min_value=0, required=False)

    class Meta:
        model = PerfilUsuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Quando a página carrega, procuramos a ofensiva do usuário e preenchemos os campos
        if self.instance and self.instance.pk and self.instance.usuario:
            try:
                perfil_gamificacao = self.instance.usuario.perfil_gamificacao
                self.fields['ofensiva'].initial = perfil_gamificacao.sequencia_dias_ativos
                self.fields['recorde'].initial = perfil_gamificacao.maior_sequencia_historica
            except ObjectDoesNotExist:
                self.fields['ofensiva'].initial = 0
                self.fields['recorde'].initial = 0

    def save(self, commit=True):
        # Salva os dados normais do PerfilUsuario (Acessibilidade, etc)
        perfil_usuario = super().save(commit=commit)
        
        # Intercepta os dados do foguinho e salva lá no aplicativo de Gamificação!
        if perfil_usuario.usuario:
            perfil_gamificacao, _ = PerfilGamificacao.objects.get_or_create(usuario=perfil_usuario.usuario)
            
            nova_ofensiva = self.cleaned_data.get('ofensiva')
            novo_recorde = self.cleaned_data.get('recorde')
            
            if nova_ofensiva is not None:
                perfil_gamificacao.sequencia_dias_ativos = nova_ofensiva
            if novo_recorde is not None:
                perfil_gamificacao.maior_sequencia_historica = novo_recorde
                
            perfil_gamificacao.save()
            
        return perfil_usuario


# 2. Registramos o Admin usando o nosso formulário
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    form = PerfilUsuarioForm
    
    # Adicionamos a coluna "mostrar_ofensiva" na tabela geral para você bater o olho e já ver
    list_display = ("usuario", "keycloak_id", "tamanho_texto", "mostrar_ofensiva")
    readonly_fields = ("keycloak_id", "usuario")
    search_fields = ("usuario__username", "keycloak_id")
    
    # Organiza visualmente a tela de edição
    fieldsets = (
        ("Informações Básicas", {
            "fields": ("usuario", "keycloak_id", "data_nascimento")
        }),
        ("Configurações de Acessibilidade", {
            "fields": ("tamanho_texto", "tamanho_botao", "assistencia_motora")
        }),
        ("Gamificação (Editável)", {
            "fields": ("ofensiva", "recorde"),
            "description": "Modifique os valores abaixo para corrigir manualmente bugs de ofensiva do usuário."
        }),
    )

    # Essa função pega o número lá da outra tabela apenas para exibir na lista geral
    def mostrar_ofensiva(self, obj):
        try:
            return f"🔥 {obj.usuario.perfil_gamificacao.sequencia_dias_ativos} dias"
        except ObjectDoesNotExist:
            return "Sem dados"
    mostrar_ofensiva.short_description = "Ofensiva Atual"