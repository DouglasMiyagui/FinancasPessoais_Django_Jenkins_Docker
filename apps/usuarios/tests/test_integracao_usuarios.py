from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestIntegraçãoUsuarios(TestCase):

    def setUp(self):
        self.client = Client()
        
    def test_cadastro_login_dashboard_logout(self):
        """Testa o fluxo de cadastro, login, dashboard e logout de um usuário"""
        
        # Testa o cadastro de um usuário
        self.assertEqual(User.objects.count(), 0)
        response = self.client.post(reverse('cadastrar_usuario'), {
            'nome': 'teste',
            'email': 'teste@teste.com',
            'password': 'teste123',
            'password2': 'teste123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(User.objects.count(), 1)

        # Testa o login de um usuário
        self.assertEqual(User.objects.count(), 1)
        response = self.client.post(reverse('login'), {
            'email': 'teste@teste.com',
            'senha': 'teste123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))      

        # Testa o dashboard de um usuário
        self.assertEqual(User.objects.count(), 1)
        self.client.login(username='teste', password='teste123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/dashboard.html')

        # Testa o logout de um usuário
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(User.objects.count(), 1)