from django.test import TestCase
from django.shortcuts import reverse
from .views import FormularioCSV
# Create your tests here.

class TestForm(TestCase):
    def testFormBien(self):
        datos = {'csv': 'buggy', 'csv_paswd': 'flores00'}
        form = FormularioCSV(datos)
        self.assertTrue(form.is_valid())

    def testFormMalo(self):
        datos = {'csv': '', 'csv_paswd': 'flores00'}
        form = FormularioCSV(datos)
        self.assertFalse(form.is_valid())