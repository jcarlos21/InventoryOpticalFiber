from netbox.forms import NetBoxModelForm
from .models import Fornecedor, TipoBobina, Bobina, Requisicao, QuantidadeFibraCabo, FibraRequisitada
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from django.utils.translation import gettext_lazy as _


class FornecedorForm(NetBoxModelForm):
    # comments = CommentField()
    class Meta:
        model = Fornecedor
        fields = ('nome_fornecedor', 'email', 'telefone', 'endereco_site', 'comments')
        labels = {
            'nome_fornecedor': _('Nome'),
            'email': _('E-mail'),
            'endereco_site': _('Endereço Eletrônico'),
        }

class TipoBobinaForm(NetBoxModelForm):
    # comments = CommentField()
    class Meta:
        model = TipoBobina
        fields = ('descricao', 'comments')
        labels = {
            'descricao': _('Status da Bobina'),
        }

class QuantidadeFibraCaboForm(NetBoxModelForm):
    class Meta:
        model = QuantidadeFibraCabo
        fields = ('quantidade', 'comments')

class BobinaForm(TipoBobinaForm, QuantidadeFibraCaboForm, NetBoxModelForm):
    nome_fornecedor = DynamicModelChoiceField(
        queryset=Fornecedor.objects.all()
    )
    fieldsets = (
        ('Parâmetros da Bobina', ('modelo', 'quantidade_fibras', 'id_privado', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'tipo_bobina', 'tags')),
        # ('Status da Bobina', ('descricao')),
    )
    class Meta:
        model = Bobina
        fields = [
            'modelo', 'quantidade_fibras', 'id_privado', 'lote_cabo', 'nome_fornecedor', 'metragem_inicial', 'metragem_final', 'tipo_bobina', 'tags'
        ]

class RequisicaoForm(NetBoxModelForm):
    class Meta:
        model = Requisicao
        fields = ('ordem_de_servico', 'imagem_OS')
        labels = {
            'ordem_de_servico': _('Ordem de Serviço'),
            'imagem_OS': _('Imagem da OS'),
        }

class FibraRequisitadaForm(NetBoxModelForm):
    class Meta:
        model = FibraRequisitada
        fields = ('bobina', 'metragem_requisitada', 'ordem_de_servico', 'imagem_corte_cabo')


# FormsFilterSets

# Bobinas:

class BobinaFilterForm(NetBoxModelFilterSetForm):
    model = Bobina

    quantidade_fibras = forms.ModelMultipleChoiceField(
        queryset=Bobina.objects.all(),
        required=False
    )
    lote_cabo = forms.ModelMultipleChoiceField(
        queryset=Bobina.objects.all(),
        required=False
    )
    nome_fornecedor = forms.ModelMultipleChoiceField(
        queryset=Fornecedor.objects.all(),
        required=False
    )

# Fornecedor

class FornecedorFilterForm(NetBoxModelFilterSetForm):
    model = Fornecedor
    nome_fornecedor = forms.ModelMultipleChoiceField(
        queryset=Fornecedor.objects.all(),
        required=False
    )

# Requisicao

class RequisicaoFilterForm(NetBoxModelFilterSetForm):
    model = Requisicao
    ordem_de_servico = forms.ModelMultipleChoiceField(
        queryset=Requisicao.objects.all(),
        required=False
    )