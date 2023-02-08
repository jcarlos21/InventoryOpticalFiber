import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Bobina

class BobinaTable(NetBoxTable):
    codBobinaAno = tables.Column(
            linkify=True
        )
    descricao = ChoiceFieldColumn()
    
    class Meta(NetBoxTable.Meta):
        model = Bobina
        fields = ('pk', 'id', 'codBobina', 'codBobinaAno', 'quantidadeFibras', 'descricao', 'actions')
        default_columns = ('id', 'codBobina', 'quantidadeFibras')

    