from django.test import SimpleTestCase
from django.urls import reverse, resolve
from usuarios.views import *

class TestUsuariosURLs(SimpleTestCase):
    """Testa as URLs do app usuarios"""

    def test_rota_url_para_view_cadastrar_usuario(self):
        """Testa se cadastrar_usuario da aplicação utiliza a função cadastrar_usuario da view"""
        url = reverse('cadastrar_usuario')
        self.assertEqual(resolve(url).func, cadastrar_usuario)

    def test_rota_url_para_view_login(self):
        """Testa se login da aplicação utiliza a função login da view"""
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)
    
    def test_rota_url_para_view_logout(self):
        """Testa se logout da aplicação utiliza a função logout da view"""
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_rota_url_para_view_dashboard(self):
        """Testa se dashboard da aplicação utiliza a função dashboard da view"""
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)