from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando nemo',
            data_lancamento = '2003-07-04',
            tipo = 'F',
            likes = 100,
            dislikes = 35
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_campos_serializados(self):
        """Teste para verificar os campos serializados"""

        dados = self.serializer.data
        # Cria uma coleção dos elementos em dados.keys() com a função set()
        # e compara com os campos do serializador.
        self.assertEquals(set(dados.keys()), set(['titulo', 'data_lancamento', 'tipo', 'likes']))

    def test_conteudo_campos_serializado(self):
        """Teste que verifica o conteúdo dos campos serializados"""

        dados = self.serializer.data
        self.assertEquals(dados['titulo'], self.programa.titulo)
        self.assertEquals(dados['tipo'], self.programa.tipo)
        self.assertEquals(dados['data_lancamento'], self.programa.data_lancamento)
        self.assertEquals(dados['likes'], self.programa.likes)