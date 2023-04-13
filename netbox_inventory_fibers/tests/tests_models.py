from django.test import TestCase

from ..models import Fornecedor, Requisicao

class FornecedorTestCase(TestCase):

    def setUp(self):
        Fornecedor.objects.create(
            nome_fornecedor = 'fornecedor_de_teste',
            email = 'fornecedor_de_teste@example.com',
            telefone = 12345678,
            endereco_site = 'www.fornecedor_de_teste.com'
        )
    def test_return_str(self):
        f1 = Fornecedor.objects.get(nome_fornecedor='fornecedor_de_teste')
        self.assertEquals(f1.__str__(), 'fornecedor_de_teste')