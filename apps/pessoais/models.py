from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Receita(models.Model):
    CATEGORIA = (
        ('salario', 'Salário'),
        ('vale', 'Vale'),
        ('bonus', 'Bonus'),
        ('comissao', 'Comissão'),
        ('freelancer', 'Freelancer'),
        ('extra', 'Extra'),
    )
    FORMA = (
        ('dinheiro', 'Dinheiro'),
        ('conta', 'Conta'),
        ('outros', 'Outros'),
    )

    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIA, blank=False, null=False, default='salario')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    forma = models.CharField(max_length=20, choices=FORMA, blank=False, null=False, default='dinheiro')
    data = models.DateField(default=date.today, blank=True)
    pago = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    CATEGORIA = (
        ('alimentacao', 'Alimentação'),
        ('moradia', 'Moradia'),
        ('transporte', 'Transporte'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('lazer', 'Lazer'),
        ('extra', 'Extra'),
    )
    FORMA = (
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('transferencia', 'Transferência'),
        ('outras', 'Outras'),
    )
    
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA, blank=False, null=False, default='alimentacao')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    forma = models.CharField(max_length=20, choices=FORMA, blank=False, null=False, default='dinheiro')
    data = models.DateField(default=date.today, blank=True)
    pago = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao