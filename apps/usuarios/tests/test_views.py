from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from pessoais.models import Receita, Despesa
from usuarios.views import *
from django.contrib.auth.models import User
from django.utils import timezone

class TestUsuariosViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test',email='teste@teste.com', password='test123')
        self.user.save()
        
    def test_cadastrar_usuario(self):
        """Testa a função que cadastra um usuário no sistema"""
        response = self.client.post(reverse('cadastrar_usuario'), {
            'nome': 'teste2',
            'email': 'teste2@teste.com',
            'password': 'teste123',
            'password2': 'teste123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(User.objects.count(), 2)

    def test_login(self):
        """Testa a função que faz o login de um usuário no sistema"""
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post(reverse('login'), {
            'email': 'teste@teste.com',
            'senha': 'test123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        
    def test_logout(self):
        """Testa a função que faz o logout de um usuário no sistema"""
        self.assertEqual(User.objects.count(), 1)
        self.client.login(username='test', password='test123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_dashboard(self):
        """Testa a função que carrega os dados de receitas e despesas no dashboard de um usuário autenticado"""
        self.receita = Receita.objects.create(id=1, pessoa=self.user, descricao='teste', categoria='teste', valor=10, forma='teste', data=timezone.now(), pago='1')
        self.despesa = Despesa.objects.create(id=1, pessoa=self.user, descricao='teste', categoria='teste', valor=10, forma='teste', data=timezone.now(), pago='1')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Receita.objects.count(), 1)
        self.assertEqual(Despesa.objects.count(), 1)
        self.client.login(username='test', password='test123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')
        self.assertEqual(response.context['receitas'].count(), 1)
        self.assertEqual(response.context['despesas'].count(), 1)
        self.assertEqual(response.context['receitas'].get().valor, 10)
        self.assertEqual(response.context['despesas'].get().valor, 10)

