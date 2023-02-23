import django_tables2 as tables

from netbox.tables import NetBoxTable #, ChoiceFieldColumn
from .models import *


class FornecedorTable(NetBoxTable):
    nome_fornecedor = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Fornecedor
        fields = ('pk', 'id', 'nome_fornecedor', 'email', 'telefone')
        default_columns = ('nome_fornecedor', 'telefone')
