from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.
class ApplicationsTestCase(TestCase):

    def setUp(self):
        """
            Configuracion para pruebas de la aplicación
        """

    def form_contact(self):
        """
            Valida formulario de contacto
        """
        client = self.client
        url = client.post(reverse("url_create_contact"))
