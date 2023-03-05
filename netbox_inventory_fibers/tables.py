import django_tables2 as tables

from netbox.tables import NetBoxTable, columns #, ChoiceFieldColumn
from .models import *


class FornecedorTable(NetBoxTable):
    nome_fornecedor = tables.Column(
        linkify=True
    )
    # bobinas_count = columns.LinkedCountColumn(
    #     viewname='wireless:wirelesslan_list',
    #     url_params={'group_id': 'pk'},
    #     verbose_name='Bobinas'
    # )
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
    # bobinas_count = columns.LinkedCountColumn(
    #     viewname='wireless:wirelesslan_list',
    #     url_params={'group_id': 'pk'},
    #     verbose_name='Bobinas'
    # )
    bobinas_associadas = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = TipoBobina
        fields = ('pk', 'id', 'descricao', 'bobinas_associadas', 'comments', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'descricao', 'bobinas_associadas')


class BobinaTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Bobina
        # É preciso adicionar o nome do fornecedor (veja como que faz)
        fields = ('pk', 'id', 'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'total_metragem', 'total_estoque', 'tags', 'created', 'last_updated')
        default_columns = ('id', 'modelo', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'total_metragem', 'total_estoque')


class RequisicaoTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Requisicao
        fields = ('pk', 'id', 'bilhete_associado', 'tags', 'created', 'last_updated')
        default_columns = ('id', 'bilhete_associado')

class QuantidadeFibraCaboTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    bobinas_associadas = tables.Column()  # Contador de bobinas associadas
    class Meta(NetBoxTable.Meta):
        model = QuantidadeFibraCabo
        fields = ('pk', 'id', 'quantidade', 'bobinas_associadas', 'tags', 'created', 'last_updated')
        default_columns = ('id', 'quantidade', 'bobinas_associadas')


# Tem que fazer uma classe para 'FibraRequisitada'. Veja se dá para aproveitar algo em: https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step04-forms.md#accesslistruleform