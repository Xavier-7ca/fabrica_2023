from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo
