import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Bobina

class BobinaTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = Bobina
        fields = ('pk', 'id', 'codBobina', 'codBobinaAno', 'quantidadeFibras', 'descricao')
        default_columns = ('id', 'codBobina')