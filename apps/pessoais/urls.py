from django.urls import path
from pessoais.views.analises import *
from pessoais.views.receitas import *
from pessoais.views.despesas import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('cadastrar/receita', cadastrar_receita, name='cadastrar_receita'),
    path('apagar/receita/<int:receita_id>', apagar_receita, name='apagar_receita'),
    path('editar/receita/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualizar/receita', atualizar_receita, name='atualizar_receita'),
    path('<int:despesa_id>', despesa, name='despesa'),
    path('cadastrar/despesa', cadastrar_despesa, name='cadastrar_despesa'),
    path('apagar/despesa/<int:despesa_id>', apagar_despesa, name='apagar_despesa'),
    path('editar/despesa/<int:despesa_id>', editar_despesa, name='editar_despesa'),
    path('atualizar/despesa', atualizar_despesa, name='atualizar_despesa'),
]
