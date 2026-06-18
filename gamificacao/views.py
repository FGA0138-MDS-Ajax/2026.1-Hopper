from django.shortcuts import render

from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView

from metas.models import RegistroDiario
from .models import PerfilGamificacao


class EstatisticasView(LoginRequiredMixin, TemplateView):
    template_name = "gamificacao/estatisticas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario = self.request.user

        periodo = self.request.GET.get("periodo", "geral")

        hoje = timezone.localdate()

        registros = RegistroDiario.objects.filter(
            meta__usuario=usuario
        )

        if periodo == "semana":
            inicio = hoje - timedelta(days=6)
            registros = registros.filter(data__gte=inicio)

        elif periodo == "mes":
            registros = registros.filter(
                data__year=hoje.year,
                data__month=hoje.month,
            )

        elif periodo == "ano":
            registros = registros.filter(
                data__year=hoje.year
            )

        total_registros = registros.count()

        total_check = registros.filter(
            status_conclusao="check"
        ).count()

        total_falha = registros.filter(
            status_conclusao="falha"
        ).count()

        total_branco = registros.filter(
            status_conclusao="branco"
        ).count()

        perfil, _ = PerfilGamificacao.objects.get_or_create(
            usuario=usuario
        )

        context.update({
            "periodo": periodo,

            "total_registros": total_registros,

            "total_check": total_check,

            "total_falha": total_falha,

            "total_branco": total_branco,

            "ofensiva": perfil.sequencia_dias_ativos,

            "recorde": perfil.maior_sequencia_historica,
        })

        return context