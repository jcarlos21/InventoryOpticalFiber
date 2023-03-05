from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Fornecedor, TipoBobina, QuantidadeFibraCabo, Bobina, Requisicao, FibraRequisitada


class FornecedorSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_inventory_fibers-api:fornecedor-detail'
    )
    bobinas_associadas = serializers.IntegerField(read_only=True)
    class Meta:
        model = Fornecedor
        fields = (
            'id', 'url', 'display', 'nome_fornecedor', 'email', 'telefone',
            'endereco_site', 'comments', 'bobinas_associadas', 'tags', 'custom_fields',
            'created', 'last_updated',
        )