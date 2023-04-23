from core.views import EntradaCreateView, VeiculosListView
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth.views import LogoutView


from . import views

app_name = "core"

urlpatterns = [
    path("", login_required(VeiculosListView.as_view()), name="index"),
    path("veiculos/", login_required(VeiculosListView.as_view()), name="veiculos"),
    path("entrada/", login_required(EntradaCreateView.as_view()), name="entrada"),
    path("<str:placa>/", login_required(views.veiculo), name="veiculo"),
    path("<str:placa>/pagar/", login_required(views.pagar), name="pagar"),
    path("<str:placa>/remover/", login_required(views.remover), name="remover"),
    path(
        "/logout/",
        LogoutView.as_view(next_page="/admin/login/?next=/veiculos/"),
        name="logout",
    ),
]
