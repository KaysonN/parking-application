from django.views.generic import CreateView, ListView
from django.shortcuts import render, get_object_or_404
from .models import Veiculo
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .form import InsereVeiculoForm

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class EntradaCreateView(CreateView):
    model = Veiculo
    form_class = InsereVeiculoForm
    template_name = "entrada.html"
    success_url = reverse_lazy("core:veiculos")

class VeiculosListView(ListView):
    template_name = "veiculos.html"
    model = Veiculo
    context_object_name = "veiculos"



@login_required(login_url="/admin")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/admin")
def veiculos(request):
    return render(request, "veiculos.html")

@login_required(login_url="/admin")
def veiculo(request, placa):
    veiculos = Veiculo.objects.filter(placa=placa)
    context = {"placa": placa, "veiculos": veiculos}
    return render(request, "veiculo.html", context=context)


@login_required(login_url="/admin")
def pagar(request, placa):
    veiculos = Veiculo.objects.filter(placa=placa)
    context = {"placa": placa, "veiculos": veiculos}
    return render(request, "pagamento.html", context=context)


@login_required(login_url="/admin")
def remover(request, placa):
    veiculo = get_object_or_404(Veiculo, placa=placa)
    veiculo.delete()
    return redirect(reverse_lazy("core:veiculos"))
