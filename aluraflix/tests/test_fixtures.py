from django.test import TestCase
from aluraflix.models import Programa

class FixtureDataTestCase(TestCase):

    fixtures = ['programas_iniciais']

    def test_carregamento(self):
        programa_um = Programa.objects.get(pk=1)
        todos_os_programas = Programa.objects.all()

        self.assertEquals(programa_um.titulo, 'Coisas bizarras')
        self.assertEquals(len(todos_os_programas), 9)