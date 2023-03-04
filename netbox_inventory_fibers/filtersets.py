from netbox.filtersets import NetBoxModelFilterSet
from .models import *


class BobinaFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Bobina
        fields = ('id', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor')
    
        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)


class FornecedorFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Fornecedor
        fields = ('id', 'nome_fornecedor')
    
        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)


class RequisicaoFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Requisicao
        fields = ('id', 'bilhete_associado')
    
        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)