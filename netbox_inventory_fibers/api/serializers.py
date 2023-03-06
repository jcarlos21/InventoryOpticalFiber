from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Fornecedor, TipoBobina, QuantidadeFibraCabo, Bobina, Requisicao, FibraRequisitada


# Fornecedor
class FornecedorSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:fornecedor-detail'
    )
    bobinas_associadas = serializers.IntegerField(read_only=True)
    class Meta:
        model = Fornecedor
        fields = (
            'id', 'url', 'display', 'nome_fornecedor', 'email', 'telefone',
            'endereco_site', 'comments', 'bobinas_associadas',
            'tags', 'custom_fields', 'created', 'last_updated',
        )

class NestedFornecedorSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:fornecedor-detail'
    )
    class Meta:
        model = Fornecedor
        fields = ('id', 'url', 'display', 'nome_fornecedor')


# TipoBobina
class TipoBobinaSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:tipobobina-detail'
    )
    bobinas_associadas = serializers.IntegerField(read_only=True)
    class Meta:
        model = TipoBobina
        fields = (
            'id', 'url', 'display', 'descricao', 'comments', 'bobinas_associadas',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
class NestedTipoBobinaSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:tipobobina-detail'
    )
    class Meta:
        model = Fornecedor
        fields = ('id', 'url', 'display', 'descricao')


# Bobina
class BobinaSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:bobina-detail'
    )
    class Meta:
        model = Bobina
        fields = (
            'id', 'url', 'display', 'nome_fornecedor', 'quantidade_fibras', 'modelo',
            'tipo_bobina', 'lote_cabo', 'metragem_inicial', 'metragem_final',
            'total_metragem', 'tags', 'custom_fields', 'created', 'last_updated',
        )
