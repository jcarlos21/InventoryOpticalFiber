import django_tables2 as tables

from netbox.tables import NetBoxTable, columns #, ChoiceFieldColumn
from .models import *


class FornecedorTable(NetBoxTable):
    nome_fornecedor = tables.Column(
        linkify=True
    )
    bobinas_associadas = tables.Column()  # Contador de bobinas associadas
    class Meta(NetBoxTable.Meta):
        model = Fornecedor
        # 225343 o 'fields' torna as opções disponíveis em 'configure table'
        fields = ('pk', 'id', 'nome_fornecedor', 'email', 'telefone', 'endereco_site', 'bobinas_associadas', 'comments', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'nome_fornecedor', 'telefone', 'endereco_site', 'bobinas_associadas')


class TipoBobinaTable(NetBoxTable):
    descricao = tables.Column(
        linkify=True
    )
    bobinas_associadas = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = TipoBobina
        fields = ('pk', 'id', 'descricao', 'bobinas_associadas', 'comments', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'descricao', 'bobinas_associadas')


class BobinaTable(NetBoxTable):
    modelo = tables.Column(
        linkify=True
    )
    total_estoque = tables.Column(verbose_name = 'Disponível')
    quantidade_fibras = tables.Column(verbose_name= 'Cabo')
    nome_fornecedor = tables.Column(verbose_name = 'Fornecedor')
    lote_cabo = tables.Column(verbose_name = 'Lote')
    class Meta(NetBoxTable.Meta):
        model = Bobina
        fields = ('pk', 'id', 'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'metragem_cadastrada', 'total_estoque', 'tags', 'created', 'last_updated')
        default_columns = ('id', 'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'metragem_cadastrada', 'total_estoque')


class RequisicaoTable(NetBoxTable):
    ordem_de_servico = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Requisicao
        fields = ('pk', 'id', 'ordem_de_servico', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'id', 'ordem_de_servico', 'created')


class QuantidadeFibraCaboTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    quantidade = tables.Column(
        linkify=True
    )
    bobinas_associadas = tables.Column()  # Contador de bobinas associadas
    class Meta(NetBoxTable.Meta):
        model = QuantidadeFibraCabo
        fields = ('pk', 'id', 'quantidade', 'bobinas_associadas', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'quantidade', 'bobinas_associadas')


class FibraRequisitadaTable(NetBoxTable):
    id = tables.Column(linkify=True)
    bobina = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = FibraRequisitada
        fields = ('pk', 'id', 'bobina', 'metragem_requisitada', 'ordem_de_servico')
        default_columns = ('pk', 'id', 'bobina', 'metragem_requisitada', 'ordem_de_servico')


# Tem que fazer uma classe para 'FibraRequisitada'. Veja se dá para aproveitar algo em: https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step04-forms.md#accesslistruleform