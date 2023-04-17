from django import template
from datetime import datetime, timedelta
from core.models import Veiculo

register = template.Library()


@register.simple_tag
def pagamento(valor_estacionamento):
    # valor = Valor.objects.get(pk=1)
    valor = Veiculo.objects.get(valor_estacionamento=valor_estacionamento)

    return valor
