from django.test import TestCase


class UsuariosUrlsTest(TestCase):
    def test_login_url_resolves_and_returns_200(self):
        """
        Garante que a URL /login/ responde com status HTTP 200 e contém o texto esperado.
        """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Página de Login (Em Construção)")

    def test_registro_url_resolves_and_returns_200(self):
        """
        Garante que a URL /registro/ responde com status HTTP 200 e contém o texto esperado.
        """
        response = self.client.get('/registro/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Página de Registro (Em Construção)")

