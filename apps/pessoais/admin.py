from django.contrib import admin
from .models import Receita, Despesa

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    list_display_links = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    search_fields = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    list_filter = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    ordering = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    list_per_page = 20

admin.site.register(Receita, ListandoReceitas)

class ListandoDespesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    list_display_links = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    search_fields = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    list_filter = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    ordering = ('id', 'descricao', 'categoria', 'valor', 'forma', 'data', 'status')
    list_per_page = 20

admin.site.register(Despesa, ListandoDespesas)
