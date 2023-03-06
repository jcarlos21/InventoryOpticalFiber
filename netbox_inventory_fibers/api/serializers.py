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
        model = TipoBobina
        fields = ('id', 'url', 'display', 'descricao')


# QuantidadeFibraCabo
class QuantidadeFibraCaboSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:quantidadefibracabo-detail'
    )
    bobinas_associadas = serializers.IntegerField(read_only=True)
    class Meta:
        model = QuantidadeFibraCabo
        fields = (
            'id', 'url', 'display', 'quantidade', 'comments', 'bobinas_associadas',
            'tags', 'custom_fields', 'created', 'last_updated',
        )
class NestedQuantidadeFibraCaboSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:quantidadefibracabo-detail'
    )
    class Meta:
        model = QuantidadeFibraCabo
        fields = ('id', 'url', 'display', 'quantidade')


# Bobina
class BobinaSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:bobina-detail'
    )
    nome_fornecedor = NestedFornecedorSerializer()
    quantidade_fibras = NestedQuantidadeFibraCaboSerializer()
    tipo_bobina = NestedTipoBobinaSerializer()
    class Meta:
        model = Bobina
        fields = (
            'id', 'url', 'display', 'nome_fornecedor', 'quantidade_fibras', 'modelo',
            'tipo_bobina', 'lote_cabo', 'metragem_inicial', 'metragem_final',
            'total_metragem', 'tags', 'custom_fields', 'created', 'last_updated',
        )


# Next step: https://github.com/netbox-community/netbox-plugin-tutorial/blob/main/tutorial/step09-rest-api.md#create-the-views