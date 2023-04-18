from .models import Vehicle
from django import forms


class InsereVeiculoForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "categoria",
            "modelo",
            "cor",
            "placa",
        ]
