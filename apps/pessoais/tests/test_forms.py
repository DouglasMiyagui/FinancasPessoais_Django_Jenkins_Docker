from django.test import TestCase
from pessoais.forms import ReceitasForm, DespesasForm
from decimal import Decimal
import datetime
from django.contrib.auth.models import User
from django.test import Client

class TestForms(TestCase):

    def setUp(self):
        """Método que cria um usuário e faz login e cadastra uma receita para testar as views"""
        self.user = User.objects.create_user(username='teste', password='teste123')
        self.client = Client()
        self.client.login(username='teste', password='teste123')

    def test_receitas_form_valid_data(self):
        form = ReceitasForm(data={
            'pessoa': self.user,
            'descricao': 'teste',
            'categoria': 'salario',
            'valor': Decimal('10'),
            'forma': 'dinheiro',
            'data': datetime.datetime.now(),
            'pago': '1'
        })

        self.assertTrue(form.is_valid())

    def test_receitas_form_no_data(self):
        form = ReceitasForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_despesas_form_valid_data(self):
        form = DespesasForm(data={
            'pessoa': self.user,
            'descricao': 'moradia',
            'categoria': 'moradia',
            'valor': Decimal('10'),
            'forma': 'debito',
            'data': datetime.datetime.now(),
            'pago': '1'
        })

        self.assertTrue(form.is_valid())

    def test_despesas_form_no_data(self):
        form = DespesasForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    