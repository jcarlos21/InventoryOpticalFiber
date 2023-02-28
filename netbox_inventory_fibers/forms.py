from netbox.forms import NetBoxModelForm
from .models import Fornecedor, TipoBobina, Bobina, Requisicao
from utilities.forms.fields import CommentField


class FornecedorForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = Fornecedor
        fields = ('nome_fornecedor', 'email', 'telefone', 'endereco_site')


class TipoBobinaForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = TipoBobina
        fields = ('descricao',)


class BobinaForm(NetBoxModelForm):
    class Meta:
        model = Bobina
        fields = ('descricao', 'quantidade_fibras', 'lote_cabo', 'metragem_inicial', 'metragem_final')


class RequisicaoForm(NetBoxModelForm):
    class Meta:
        model = Requisicao
        fields = ('bilhete_associado',)

# Tem que fazer uma classe para 'FibraRequisitada'. Veja em: https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step04-forms.md#accesslistruleform