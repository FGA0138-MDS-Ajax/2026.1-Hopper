from django.utils import timezone

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from gamificacao.models import PerfilGamificacao

from .models import Categoria, Meta, RegistroDiario

ROTA_LISTAR_METAS = "metas:listar"


class ListarMetasView(LoginRequiredMixin, ListView):
    model = Meta
    template_name = "metas/listar.html"
    context_object_name = "metas"

    def get_queryset(self):
        # 1. Pega todas as metas do utilizador
        queryset = Meta.objects.filter(usuario=self.request.user)

        # 2. Verifica se existe algum filtro de categoria na URL
        categoria_id = self.request.GET.get("categoria")

        # 3. Aplica o filtro consoante a escolha
        if categoria_id == "sem_categoria":
            queryset = queryset.filter(categoria__isnull=True)
        elif categoria_id and categoria_id != "todas":
            queryset = queryset.filter(categoria_id=categoria_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Envia todas as categorias deste utilizador para o HTML desenhar os botões
        context["categorias"] = Categoria.objects.filter(usuario=self.request.user)
        # Envia qual é a aba que está ativa no momento (para pintá-la de cor forte)
        context["categoria_ativa"] = self.request.GET.get("categoria", "todas")
        return context


class CriarMetaView(LoginRequiredMixin, CreateView):
    model = Meta
    fields = ["titulo", "categoria"]
    template_name = "metas/criar.html"
    success_url = reverse_lazy(ROTA_LISTAR_METAS)

    def get_initial(self):
        initial = super().get_initial()
        cat_id = self.request.GET.get("categoria")
        if cat_id and cat_id not in ["todas", "sem_categoria"]:
            initial["categoria"] = cat_id
        return initial

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["categoria"].queryset = Categoria.objects.filter(
            usuario=self.request.user
        )
        form.fields["categoria"].empty_label = "Nenhuma (Sem Categoria)"
        return form


class DeletarMetaView(LoginRequiredMixin, DeleteView):
    model = Meta

    success_url = reverse_lazy(ROTA_LISTAR_METAS)

    template_name = "metas/deletar.html"

    def get_queryset(self):
        return Meta.objects.filter(usuario=self.request.user)


@login_required
def atualizar_status_diario(request, registro_id):

    registro = get_object_or_404(
        RegistroDiario,
        id=registro_id,
        meta__usuario=request.user,
    )

    novo_status = request.POST.get("status")
    nova_nota = request.POST.get("nota", "")

    if novo_status in ["check", "falha", "branco"]:
        registro.status_conclusao = novo_status
        
        hoje = timezone.localdate()
        
        # Só aciona a gamificação se for "check" E a data do quadradinho for exatamente HOJE
        if novo_status == "check" and registro.data == hoje:
            perfil, _ = PerfilGamificacao.objects.get_or_create(usuario=request.user)
            perfil.registrar_check_in()

    registro.nota = nova_nota
    registro.save()

    return redirect("metas:listar")


class CriarCategoriaView(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ["nome", "cor_identificacao"]
    template_name = "metas/criar_categoria.html"
    success_url = reverse_lazy("metas:listar")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["nome"].label = "Nome da Categoria"
        form.fields["cor_identificacao"].label = "Cor da Categoria"
        form.fields["cor_identificacao"].widget = forms.HiddenInput()
        form.fields["cor_identificacao"].initial = "#FF9500"
        return form


class ListarCategoriasView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "metas/listar_categoria.html"
    context_object_name = "categorias"

    def get_queryset(self):
        return Categoria.objects.filter(usuario=self.request.user)


class DeletarCategoriaView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "metas/deletar_categoria.html"
    success_url = reverse_lazy("metas:listar_categorias")

    def get_queryset(self):
        return Categoria.objects.filter(usuario=self.request.user)


class EditarMetaView(LoginRequiredMixin, UpdateView):
    model = Meta
    fields = ["titulo", "categoria"]
    template_name = "metas/editar.html"
    success_url = reverse_lazy("metas:listar")

    def get_queryset(self):
        return Meta.objects.filter(usuario=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["categoria"].queryset = Categoria.objects.filter(
            usuario=self.request.user
        )
        form.fields["categoria"].empty_label = "Nenhuma (Sem Categoria)"
        return form


class EditarCategoriaView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ["nome", "cor_identificacao"]
    template_name = "metas/editar_categoria.html"
    success_url = reverse_lazy("metas:listar_categorias")

    def get_queryset(self):
        return Categoria.objects.filter(usuario=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["nome"].label = "Nome da Categoria"
        form.fields["cor_identificacao"].label = "Cor da Categoria"
        form.fields["cor_identificacao"].widget = forms.HiddenInput()
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editando"] = True
        return context