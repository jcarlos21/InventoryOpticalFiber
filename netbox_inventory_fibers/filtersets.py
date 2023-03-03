from netbox.filtersets import NetBoxModelFilterSet
from .models import Bobina


class BobinaFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Bobina
        fields = ('id', 'quantidade_fibras', 'lote_cabo', 'nome_fornecedor')
    
        def search(self, queryset, name, value):
            return queryset.filter(description__icontains=value)