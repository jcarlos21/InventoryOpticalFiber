from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import FornecedorSerializer, TipoBobinaSerializer, QuantidadeFibraCaboSerializer, BobinaSerializer
from django.db.models import Count


class FornecedorViewSet(NetBoxModelViewSet):
    queryset = models.Fornecedor.objects.prefetch_related('tags').annotate(
        bobinas_associadas=Count('bobinas_to_fornecedor')
    )
    serializer_class = FornecedorSerializer


class TipoBobinaViewSet(NetBoxModelViewSet):
    queryset = models.TipoBobina.objects.prefetch_related('tags').annotate(
        bobinas_associadas=Count('bobinas')
    )
