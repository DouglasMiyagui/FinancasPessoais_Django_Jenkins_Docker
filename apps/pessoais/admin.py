from django.contrib import admin
from .models import Receita, Despesa

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    list_display_links = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    search_fields = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    list_filter = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    ordering = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    list_per_page = 20

admin.site.register(Receita, ListandoReceitas)

class ListandoDespesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    list_display_links = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    search_fields = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    list_filter = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    ordering = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'pago')
    list_per_page = 20

admin.site.register(Despesa, ListandoDespesas)
