from core.views import EntradaCreateView, VeiculosListView
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", VeiculosListView.as_view(), name="index"),
    path("veiculos/", VeiculosListView.as_view(), name="veiculos"),
    path("entrada/", EntradaCreateView.as_view(), name="entrada"),
    path("<str:placa>/", views.veiculo, name="veiculo"),
    path("<str:placa>/pagar/", views.pagar, name="pagar"),
    path("<str:placa>/remover/", views.remover, name="remover"),
]
