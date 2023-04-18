from django.views.generic import CreateView, ListView
from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import InsereVeiculoForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


class EntradaCreateView(CreateView):
    model = Vehicle
    form_class = InsereVeiculoForm
    template_name = "entrada.html"
    success_url = reverse_lazy("core:veiculos")


class VeiculosListView(LoginRequiredMixin, ListView):
    login_url = "login"
    redirect_field_name = "next"
    template_name = "veiculos.html"
    model = Vehicle
    context_object_name = "veiculos"

    def get_queryset(self):
        placa_desejada = self.request.GET.get("placa", "")
        queryset = super().get_queryset()
        if placa_desejada:
            queryset = queryset.filter(placa=placa_desejada)
        return queryset


@login_required(login_url="/admin")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/admin")
def veiculos(request):
    return render(request, "veiculos.html")


@login_required(login_url="/admin")
def veiculo(request, placa):
    veiculos = Vehicle.objects.filter(placa=placa)
    context = {"placa": placa, "veiculos": veiculos}
    return render(request, "veiculo.html", context=context)


@login_required(login_url="/admin")
def pagar(request, placa):
    veiculos = Vehicle.objects.filter(placa=placa)
    context = {"placa": placa, "veiculos": veiculos}
    return render(request, "pagamento.html", context=context)


@login_required(login_url="/admin")
def remover(request, placa):
    veiculo = get_object_or_404(Vehicle, placa=placa)
    veiculo.delete()
    return redirect(reverse_lazy("core:veiculos"))
