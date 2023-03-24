from django.db import models
from datetime import date
from django.contrib.auth.models import User
from pessoais.choices import *

class Receita(models.Model):  
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_RECEITA, blank=False, null=False, default='salario')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    forma = models.CharField(max_length=20, choices=FORMA_RECEITA, blank=False, null=False, default='dinheiro')
    data = models.DateField(default=date.today, blank=True)
    pago = models.CharField(max_length=1, choices=PAGO_RECEITA, blank=False, null=False, default='1')

    def __str__(self):
        return self.pago
    
    def __str__(self):
        return self.descricao

    def __str__(self):
        return self.forma

class Despesa(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_DESPESA, blank=False, null=False, default='alimentacao')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    forma = models.CharField(max_length=20, choices=FORMA_DESPESA, blank=False, null=False, default='dinheiro')
    data = models.DateField(default=date.today, blank=True)
    pago = models.CharField(max_length=1, choices=PAGO_DESPESA, blank=False, null=False, default='1')

    def __str__(self):
        return self.descricao

    def __str__(self):
        return self.forma

    def __str__(self):
        return self.pago
