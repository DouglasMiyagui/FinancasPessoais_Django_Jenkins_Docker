from django.test import TestCase, RequestFactory
from pessoais.models import Receita, Despesa
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

class UsuariosTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_login(self):
            """Testa o cadastro do usuário e o login do mesmo"""
            self.user = User.objects.create_user(
                username='test',email='teste@teste.com', password='test')
            self.user.save()

            # Logging
            login = self.client.login(username='test', password='test')
            self.assertEquals(login, True)
