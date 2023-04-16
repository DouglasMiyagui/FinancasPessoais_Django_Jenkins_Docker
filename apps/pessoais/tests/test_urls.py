from django.test import TestCase, RequestFactory
from django.urls import reverse
from pessoais.views.analises import *

class PessoaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_para_view_index(self):
        """Testa se home da aplicação utiliza a função index da view"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('pessoais/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)