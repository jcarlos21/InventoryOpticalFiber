from netbox.forms import NetBoxModelForm
from .models import Fornecedor, TipoBobina, Bobina, Requisicao


class FornecedorForm(NetBoxModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome_fornecedor', 'email', 'telefone', 'endereco_site')


class TipoBobina(NetBoxModelForm):
    class Meta:
        model = TipoBobina
        fields = ('descricao')


class BobinaForm(NetBoxModelForm):
    class Meta:
        model = Bobina
        fields = ('descricao', 'quantidade_fibras', 'lote_cabo', 'metragem_inicial', 'metragem_final')


