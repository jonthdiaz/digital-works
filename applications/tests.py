# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Contact
import json


# Create your tests here.
class ApplicationsTestCase(TestCase):

    def setUp(self):
        """
            Configuracion para pruebas de la aplicación
        """

    def form_contact(self):
        """
            Valida formulario de contacto cuando no se ingresa info
        """
        data = {
            'name': '',
            'email': '',
            'observations': '',
        }
        client = self.client
        response = client.post(reverse("url_create_contact"), data)

        content = json.loads(response.content.decode())
        # valido que los tres campos generen errores
        self.assertTrue("name" in content['error'])
        self.assertTrue("email" in content['error'])
        self.assertTrue("observations" in content['error'])
        # valido que la respuesta sea False
        self.assertFalse(content['success'])

    def form_contact_case_done(self):
        """
            Valida formulario de contacto cuando no se ingresa info
        """
        data = {
            'name': 'jonathan',
            'email': 'jonthdiaz@gmail.com',
            'observations': 'Este programa es una chimba',
        }
        client = self.client
        response = client.post(reverse("url_create_contact"), data)

        content = json.loads(response.content.decode())

        # valido que la respuesta sea True
        self.assertTrue(content['success'])

        # Verifico que exista el registro
        self.assertTrue(Contact.objects.filter(
            email="jonthdiaz@gmail").exixts())
