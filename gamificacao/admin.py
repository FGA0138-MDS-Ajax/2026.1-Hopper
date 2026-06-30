from django.contrib import admin
from .models import PerfilGamificacao, FraseInspiradora

@admin.register(FraseInspiradora)
class FraseInspiradoraAdmin(admin.ModelAdmin):
    list_display = ("texto", "autor")
    search_fields = ("texto", "autor")