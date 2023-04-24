from django.views.generic import CreateView, ListView
from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import InsereVeiculoForm


# Cria uma nova entrada de veículo
class EntradaCreateView(CreateView):
    model = Vehicle
    form_class = InsereVeiculoForm
    template_name = "entrada.html"
    success_url = reverse_lazy("core:veiculos")


# Classe para exibir a lista de veículos
class VeiculosListView(LoginRequiredMixin, ListView):
    login_url = "login"
    redirect_field_name = "next"
    template_name = "veiculos.html"
    model = Vehicle
    context_object_name = "veiculos"


# Função para exibir a página inicial da aplicação
def index(request):
    return render(request, "index.html")


# Função para exibir informações de um veículo específico
def veiculo(request, placa):
    veiculos = Vehicle.objects.filter(placa=placa)
    context = {"placa": placa, "veiculos": veiculos}
    return render(request, "veiculo.html", context=context)


# Função para exibir a página de pagamento de um veículo
def pagar(request, placa):
    veiculos = Vehicle.objects.filter(placa=placa)
    context = {"placa": placa, "veiculos": veiculos}
    return render(request, "pagamento.html", context=context)


# Função para remover um veículo do sistema
def remover(request, placa):
    veiculo = get_object_or_404(Vehicle, placa=placa)
    veiculo.delete()
    return redirect(reverse_lazy("core:veiculos"))
