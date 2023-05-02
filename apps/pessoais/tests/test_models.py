from django.test import TestCase, RequestFactory
from pessoais.models import Receita, Despesa
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse


class PessoaisReceitasModelTestCase(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test_user',
            'password': 'secret'}
        user = User.objects.create_user(**self.credentials)
        self.client.force_login(user)
        self.user_id = user
    
    
        self.receita = Receita.objects.create(
            pessoa = user,
            descricao = 'mercado',
            categoria = 'alimentacao',
            valor = 123.00,
            forma = 'dinheiro',
            data = '2022-06-09',
            pago = '1',
        )
    
    def test_receita_cadastrada_no_banco_de_dados_com_sucesso(self):
        """Teste que verifica se a receita do usurário logado foi cadastrada com suas características"""
        self.assertEqual(self.receita.descricao, 'mercado')
        self.assertEqual(self.receita.data, '2022-06-09')

class PessoaisDespesasModelTestCase(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'test_user',
            'password': 'secret'}
        user = User.objects.create_user(**self.credentials)
        self.client.force_login(user)
        self.user_id = user

        self.despesa = Despesa.objects.create(
            pessoa = user,
            descricao = 'salario',
            categoria = 'salario',
            valor = 123.00,
            forma = 'dinheiro',
            data = '2022-06-09',
            pago = '1',
        )
    
    def test_despesa_cadastrada_com_sucesso(self):
        """Teste que verifica se a despesa do usurário logado foi cadastrada com suas características"""
        self.assertEqual(self.despesa.descricao, 'salario')
        self.assertEqual(self.despesa.forma, 'dinheiro')
            
        


       