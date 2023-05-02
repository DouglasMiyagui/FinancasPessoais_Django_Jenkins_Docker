from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pessoais.views.analises import *
from pessoais.views.despesas import *
from pessoais.views.receitas import *

class TestPessoaisURLS(SimpleTestCase):
    """Classe de testes das urls da aplicação pessoais"""

    # Analises

    def test_rota_url_para_view_index(self):
        """Testa se home da aplicação utiliza a função index da view"""
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    # Receitas
    
    def test_rota_url_para_view_receita(self):
        """Testa se receita da aplicação utiliza a função receita da view"""
        url = reverse('receita', args=[1])
        self.assertEqual(resolve(url).func, receita)

    def test_rota_url_para_view_cadastrar_receita(self):
        """Testa se cadastrar_receita da aplicação utiliza a função cadastrar_receita da view"""
        url = reverse('cadastrar_receita')
        self.assertEqual(resolve(url).func, cadastrar_receita)

    def test_rota_url_para_view_apagar_receita(self):
        """Testa se apagar_receita da aplicação utiliza a função apagar_receita da view"""
        url = reverse('apagar_receita', args=[1])
        self.assertEqual(resolve(url).func, apagar_receita)

    def test_rota_url_para_view_editar_receita(self):
        """Testa se editar_receita da aplicação utiliza a função editar_receita da view"""
        url = reverse('editar_receita', args=[1])
        self.assertEqual(resolve(url).func, editar_receita)

    def test_rota_url_para_view_atualizar_receita(self):
        """Testa se atualizar_receita da aplicação utiliza a função atualizar_receita da view"""
        url = reverse('atualizar_receita')
        self.assertEqual(resolve(url).func, atualizar_receita)

    # Despesas

    def test_rota_url_para_view_cadastrar_despesa(self):
        """Testa se cadastrar_despesa da aplicação utiliza a função cadastrar_despesa da view"""
        url = reverse('cadastrar_despesa')
        self.assertEqual(resolve(url).func, cadastrar_despesa)

    def test_rota_url_para_view_apagar_despesa(self):
        """Testa se apagar_despesa da aplicação utiliza a função apagar_despesa da view"""
        url = reverse('apagar_despesa', args=[1])
        self.assertEqual(resolve(url).func, apagar_despesa)

    def test_rota_url_para_view_editar_despesa(self):
        """Testa se editar_despesa da aplicação utiliza a função editar_despesa da view"""
        url = reverse('editar_despesa', args=[1])
        self.assertEqual(resolve(url).func, editar_despesa)

    def test_rota_url_para_view_atualizar_despesa(self):
        """Testa se atualizar_despesa da aplicação utiliza a função atualizar_despesa da view"""
        url = reverse('atualizar_despesa')
        self.assertEqual(resolve(url).func, atualizar_despesa)
        
    

    