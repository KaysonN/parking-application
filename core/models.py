from django.db import models


class Vehicle(models.Model):
    CATEGORIAS = [("a", "Moto"), ("b", "Carro"), ("c", "Pesado")]

    modelo = models.CharField("modelo", max_length=100, null=False)
    cor = models.CharField("cor", max_length=50, null=False)
    placa = models.CharField("placa", max_length=8, null=False)
    ativo = models.BooleanField("ativo", default=True)
    data_entrada = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(
        "categoria", max_length=100, null=False, choices=CATEGORIAS
    )
    valor_estacionamento = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.placa

    def save(self, *args, **kwargs):
        if self.categoria == "a":
            self.valor_estacionamento = 5
        elif self.categoria == "b":
            self.valor_estacionamento = 10
        elif self.categoria == "c":
            self.valor_estacionamento = 20
        super(Vehicle, self).save(*args, **kwargs)


class Entry(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vehicle.data_entrada)
