from django.test import TestCase

from ..models import Bobina, QuantidadeFibraCabo, Fornecedor, TipoBobina, Requisicao, FibraRequisitada


class RequisicaoTestCase(TestCase):

    def setUp(self):
        f1 = Fornecedor.objects.create(
            nome_fornecedor = 'fornecedor_de_teste',
            email = 'fornecedor_de_teste@example.com',
            telefone = 12345678,
            endereco_site = 'www.fornecedor_de_teste.com'
        )
        q1 = QuantidadeFibraCabo.objects.create(
            quantidade = '36FO'
        )
        tp1 = TipoBobina.objects.create(
            descricao = 'Fechada'
        )
        req1 = Requisicao.objects.create(
            ordem_de_servico = '2023.02-BR15',
            imagem_OS = '/uploads/Screenshot_from_2023-02-26_21-48-57_LqXGqhw.png'
        )
      
        b1 = Bobina.objects.create(
            nome_fornecedor = f1,
            quantidade_fibras = q1,
            modelo = 'AS G 80',
            tipo_bobina = tp1,
            lote_cabo = '197',
            metragem_cadastrada = 650
        )
        FibraRequisitada.objects.create(
            bobina = b1,
            metragem_requisitada = 100,
            imagem_corte_cabo = '/uploads/Screenshot_from_2023-02-26_21-48-57_LqXGqhw.png',
            ordem_de_servico = req1
        )
    
    def test_return_str(self):
        fb1 = FibraRequisitada.objects.get(id_customizado='REQ0001_23')
        self.assertEquals(fb1.__str__(), 'REQ0001_23')