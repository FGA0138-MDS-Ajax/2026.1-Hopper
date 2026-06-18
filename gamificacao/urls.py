from django.urls import path

from .views import EstatisticasView

app_name = "gamificacao"

urlpatterns = [
    path(
        "",
        EstatisticasView.as_view(),
        name="estatisticas",
    ),
]