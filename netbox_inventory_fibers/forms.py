from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import Bobina

from utilities.forms.fields import CommentField

class BobinaForm(NetBoxModelForm):

    quantidadeFibras = CommentField()

    class Meta:
        model = Bobina
        fields = ('codBobina', 'codBobinaAno', 'quantidadeFibras', 'descricao')