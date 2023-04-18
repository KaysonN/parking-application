from django import template
from datetime import datetime
from decimal import Decimal
from math import ceil
from core.models import Vehicle

register = template.Library()

@register.simple_tag
def pagamento(placa):
    veiculo = Vehicle.objects.get(placa=placa)
    valor_estacionamento = Decimal(str(veiculo.valor_estacionamento))
    entrada = veiculo.data_entrada
    saida = datetime.now()
    
    tempo_permanencia = saida - entrada
    segundos_permanencia = tempo_permanencia.total_seconds()
    horas_permanencia = ceil(segundos_permanencia / 3600)
    
    if horas_permanencia < 1:
        horas_permanencia = 1  # mínimo de 1 hora
        
    valor_final = Decimal(str(horas_permanencia)) * valor_estacionamento
    valor_final = valor_final.quantize(Decimal('0.01'))

    return valor_final
