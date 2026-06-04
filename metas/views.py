from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Meta, RegistroDiario

class ListarMetasView(LoginRequiredMixin, ListView):
    model = Meta
    context_object_name = "metas"
    template_name = "metas/listar.html"

    def get_queryset(self):
        return Meta.objects.filter(usuario=self.request.user)

class CriarMetaView(LoginRequiredMixin, CreateView):
    model = Meta

    fields = [
        "titulo",
        "categoria"
    ]

    template_name = "metas/criar.html"

    success_url = reverse_lazy("metas:listar")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class DeletarMetaView(LoginRequiredMixin, DeleteView):
    model = Meta

    success_url = reverse_lazy("metas:listar")

    template_name = "metas/deletar.html"

    def get_queryset(self):
        return Meta.objects.filter(usuario=self.request.user)

def atualizar_status_diario(request, registro_id):

    registro = get_object_or_404(
        RegistroDiario,
        id=registro_id,
        meta__usuario=request.user,
    )

    novo_status = request.POST.get("status")

    if novo_status in ["check", "falha", "branco"]:
        registro.status_conclusao = novo_status
        registro.save()

    return redirect("metas:listar")