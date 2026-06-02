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
]
