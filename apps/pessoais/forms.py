from django import forms
from pessoais.choices import *
from datetime import date
from .models import Receita, Despesa
from django.forms.widgets import NumberInput

class ReceitasForm(forms.ModelForm):  
    descricao = forms.CharField(label='Descrição', max_length=200)
    categoria = forms.ChoiceField(label='Categoria', required=False, choices=CATEGORIA_RECEITA)
    valor = forms.DecimalField(label='Valor')
    forma = forms.ChoiceField(label='Forma', required=False, choices=FORMA_RECEITA)
    data = forms.DateField(label='Data', initial=date.today, widget=NumberInput(attrs={'type': 'date'}))
    estado = forms.ChoiceField(label='Status', required=False, choices=ESTADO_RECEITA)

    class Meta:
        model = Receita
        fields = ('descricao', 'categoria', 'valor', 'forma', 'data', 'estado')


class DespesasForm(forms.ModelForm):
    descricao = forms.CharField(label='Descrição', max_length=200)
    categoria = forms.ChoiceField(label='Categoria', required=False, choices=CATEGORIA_DESPESA)
    valor = forms.DecimalField(label='Valor')
    forma = forms.ChoiceField(label='Forma', required=False, choices=FORMA_DESPESA)
    data = forms.DateField(label='Data', initial=date.today, widget=NumberInput(attrs={'type': 'date'}))
    estado = forms.ChoiceField(label='Status', required=False, choices=ESTADO_DESPESA)

    class Meta:
        model = Despesa
        fields = ('descricao', 'categoria', 'valor', 'forma', 'data', 'estado')