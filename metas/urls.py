from django.urls import path

from . import views

app_name = "metas"

urlpatterns = [
    # Read - Lista a tela inicial com as metas (e os calendários expansíveis)
    path("", views.ListarMetasView.as_view(), name="listar"),
    # Cria - Tela para cadastrar metas novas
    path("nova/", views.CriarMetaView.as_view(), name="criar"),
    # Delete - Deleta a meta inteira
    path("<int:pk>/deletar/", views.DeletarMetaView.as_view(), name="deletar"),
    # Update - Marcar o Registro Diário como feito/não feito
    path(
        "registro/<int:registro_id>/atualizar/",
        views.atualizar_status_diario,
        name="atualizar_registro",
    ),
    # Criar Categorias
    path("categoria/nova/", views.CriarCategoriaView.as_view(), name="criar_categoria"),
    # Listar Categorias
    path("categorias/", views.ListarCategoriasView.as_view(), name="listar_categorias"),
    # Apagar Categoria
    path(
        "categoria/<int:pk>/deletar/",
        views.DeletarCategoriaView.as_view(),
        name="deletar_categoria",
    ),
    # Editar Metas
    path("<int:pk>/editar/", views.EditarMetaView.as_view(), name="editar"),
    # Editar Categorias
    path(
        "categorias/<int:pk>/editar/",
        views.EditarCategoriaView.as_view(),
        name="editar_categoria",
    ),
]
