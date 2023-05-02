from pessoais.models import Receita, Despesa
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.utils import timezone


class TestPessoaisViews(TestCase):
    """Classe de testes das views da aplicação pessoais"""
    
    def setUp(self):
        """Método que cria um usuário e faz login e cadastra uma receita para testar as views"""
        self.user = User.objects.create_user(username='teste', password='teste123')
        self.client = Client()
        self.client.login(username='teste', password='teste123')
        self.receita = Receita.objects.create(id=1, pessoa=self.user, descricao='teste', categoria='teste', valor=10, forma='teste', data=timezone.now(), pago='1')
        self.despesa = Despesa.objects.create(id=1, pessoa=self.user, descricao='teste', categoria='teste', valor=10, forma='teste', data=timezone.now(), pago='1')

    # Receitas

    def test_receita(self):
        """Testa a função que pega a receita pelo id e carrega na página dashboard.html"""    
        response = self.client.get(reverse('receita', args=[self.receita.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')

    def test_cadastrar_receita(self):
        """Testa a função que cadastra a receita, redireciona para a url dashboard que retorna a página dashboard.html"""
        response = self.client.get(reverse('cadastrar_receita'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')

    def test_apagar_receita(self):
        """Testa a função que apaga a receita e redireciona para a url dashboard"""
        response = self.client.get(reverse('apagar_receita', args=[self.receita.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.client.post('/apagar/receita/', {'id': 1})
        self.assertEqual(Receita.objects.count(), 0)

    def test_editar_receita(self):
        """Testa a função que pega a receita pelo id e carrega no formulário para editar na página editar_receita.html"""
        response = self.client.get(reverse('editar_receita', args=[self.receita.id]))
        self.assertEqual(self.receita.descricao, 'teste')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pessoais/editar_receita.html')
        self.client.post('/editar/receita/', {'id': 1})
        self.assertEqual(Receita.objects.count(), 1)

    def test_atualizar_receita(self):
        """Testa a função que recebe do formulário a receita editada, atualiza os dados gravando no banco de dados e redireciona para a url dashboard"""
        response = self.client.get(reverse('atualizar_receita'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')
        self.client.post('/atualizar/receita/', {'id': 1})
        self.assertEqual(Receita.objects.count(), 1)

    # Despesas

    def test_despesa(self):
        """Testa a função que pega a despesa pelo id e carrega na página dashboard.html"""
        response = self.client.get(reverse('despesa', args=[self.despesa.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')

    def test_cadastrar_despesa(self):
        """Testa a função que cadastra a despesa, redireciona para a url dashboard que retorna a página dashboard.html"""
        response = self.client.get(reverse('cadastrar_despesa'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')

    def test_apagar_despesa(self):
        """Testa a função que apaga a despesa e redireciona para a url dashboard"""
        response = self.client.get(reverse('apagar_despesa', args=[self.despesa.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.client.post('/apagar/despesa/', {'id': 1})
        self.assertEqual(Despesa.objects.count(), 0)

    def test_editar_despesa(self):
        """Testa a função que pega a despesa pelo id e carrega no formulário para editar na página editar_despesa.html"""
        response = self.client.get(reverse('editar_despesa', args=[self.despesa.id]))
        self.assertEqual(self.despesa.descricao, 'teste')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pessoais/editar_despesa.html')
        self.client.post('/editar/despesa/', {'id': 1})
        self.assertEqual(Despesa.objects.count(), 1)

    def test_atualizar_despesa(self):
        """Testa a função que recebe do formulário a despesa editada, atualiza os dados gravando no banco de dados e redireciona para a url dashboard"""
        response = self.client.get(reverse('atualizar_despesa'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')
        self.client.post('/atualizar/despesa/', {'id': 1})
        self.assertEqual(Despesa.objects.count(), 1)

    





