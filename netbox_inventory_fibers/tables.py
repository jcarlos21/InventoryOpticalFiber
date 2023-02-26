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
    class Meta(NetBoxTable.Meta):
        model = Fornecedor
        # 225343 o 'fields' torna as opções disponíveis em 'configure table'
        fields = ('pk', 'id', 'nome_fornecedor', 'email', 'telefone', 'endereco_site', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'nome_fornecedor', 'telefone', 'endereco_site')


class TipoBobinaTable(NetBoxTable):
    descricao = tables.Column(
        linkify=True
    )
    # bobinas_count = columns.LinkedCountColumn(
    #     viewname='wireless:wirelesslan_list',
    #     url_params={'group_id': 'pk'},
    #     verbose_name='Bobinas'
    # )
    bobina_count = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = TipoBobina
        fields = ('pk', 'id', 'descricao', 'bobina_count', 'tags', 'created', 'last_updated')
        default_columns = ('pk', 'descricao', 'bobina_count')


class BobinaTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Bobina
        # É preciso adicionar o nome do fornecedor (veja como que faz)
        fields = ('pk', 'id', 'descricao', 'quantidade_fibras', 'lote_cabo', 'metragem_inicial', 'metragem_final', 'total_metragem', 'total_estoque', 'tags', 'created', 'last_updated')
        default_columns = ('id', 'descricao', 'quantidade_fibras', 'lote_cabo', 'metragem_inicial', 'metragem_final', 'total_metragem', 'total_estoque')


class RequisicaoTable(NetBoxTable):
    id = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Requisicao
        fields = ('pk', 'id', 'bilhete_associado', 'tags', 'created', 'last_updated')
        default_columns = ('id', 'bilhete_associado')


# Tem que fazer uma classe para 'FibraRequisitada'. Veja se dá para aproveitar algo em: https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step04-forms.md#accesslistruleform