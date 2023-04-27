import django_tables2 as tables

from netbox.tables import NetBoxTable, columns #, ChoiceFieldColumn
from .models import *


class FornecedorTable(NetBoxTable):
    nome_fornecedor = tables.Column(
        linkify=True
    )
    bobinas_associadas = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = Fornecedor
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
    total_estoque = tables.Column(verbose_name = 'Disponível')
    quantidade_fibras = tables.Column(verbose_name= 'Cabo')
    nome_fornecedor = tables.Column(verbose_name = 'Fornecedor')
    lote_cabo = tables.Column(verbose_name = 'Lote')
    special_id = tables.Column(linkify=True, verbose_name = 'ID Bobina')
    tipo_bobina = tables.Column(verbose_name = 'Tipo')
    metragem_cadastrada = tables.Column(verbose_name = 'Met. Cadastrada')
    class Meta(NetBoxTable.Meta):
        model = Bobina
        fields = ('pk', 'id', 'special_id', 'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'tipo_bobina', 'metragem_cadastrada', 'total_estoque', 'tags', 'created', 'last_updated')
        default_columns = ('special_id', 'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'tipo_bobina', 'metragem_cadastrada', 'total_estoque')


class RequisicaoTable(NetBoxTable):
    ordem_de_servico = tables.Column(
        linkify=True
    )
    requisicoes_associadas = tables.Column(verbose_name = 'Requisições Associadas')
    imagem_OS = tables.Column(verbose_name = 'Arquivo da OS')
    class Meta(NetBoxTable.Meta):
        model = Requisicao
        fields = ('pk', 'id', 'ordem_de_servico', 'requisicoes_associadas', 'imagem_OS', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'id', 'ordem_de_servico', 'requisicoes_associadas', 'created')


class QuantidadeFibraCaboTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    quantidade = tables.Column(
        linkify=True
    )
    bobinas_associadas = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = QuantidadeFibraCabo
        fields = ('pk', 'id', 'quantidade', 'bobinas_associadas', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'quantidade', 'bobinas_associadas')


class FibraRequisitadaTable(NetBoxTable):
    id = tables.Column(linkify=True)
    bobina = tables.Column(linkify=True)
    id_customizado = tables.Column(verbose_name = 'ID Requisição', linkify=True)
    metragem_requisitada = tables.Column(verbose_name = 'Metragem Requisitada (m)')
    class Meta(NetBoxTable.Meta):
        model = FibraRequisitada
        fields = ('pk', 'id', 'id_customizado', 'bobina', 'metragem_requisitada', 'ordem_de_servico', 'imagem_corte_cabo')
        default_columns = ('pk', 'id_customizado', 'metragem_requisitada', 'bobina', 'ordem_de_servico', 'imagem_corte_cabo')
