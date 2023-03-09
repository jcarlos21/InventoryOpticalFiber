from netbox.api.viewsets import NetBoxModelViewSet
from .. import filtersets, models
from .serializers import FornecedorSerializer, TipoBobinaSerializer, QuantidadeFibraCaboSerializer, BobinaSerializer, RequisicaoSerializer
from django.db.models import Count


class FornecedorViewSet(NetBoxModelViewSet):
    queryset = models.Fornecedor.objects.prefetch_related('tags').annotate(
        bobinas_associadas=Count('bobinas_to_fornecedor')
    )
    serializer_class = FornecedorSerializer
    filterset_class = filtersets.FornecedorFilterSet


class TipoBobinaViewSet(NetBoxModelViewSet):
    queryset = models.TipoBobina.objects.prefetch_related('tags').annotate(
        bobinas_associadas=Count('bobinas')
    )
    serializer_class = TipoBobinaSerializer


class QuantidadeFibraCaboViewSet(NetBoxModelViewSet):
    queryset = models.QuantidadeFibraCabo.objects.prefetch_related('tags')
    serializer_class = QuantidadeFibraCaboSerializer


class BobinaViewSet(NetBoxModelViewSet):
    queryset = models.Bobina.objects.prefetch_related(
        'nome_fornecedor', 'quantidade_fibras', 'tipo_bobina', 'tags'
    )
    serializer_class = BobinaSerializer
    filterset_class = filtersets.BobinaFilterSet


class RequisicaoViewSet(NetBoxModelViewSet):
    queryset = models.Requisicao.objects.prefetch_related('tags') # .annotate(bobinas_associadas=Count('fibrarequisitada_to_ordem_servico'))
    serializer_class = RequisicaoSerializer
    filterset_class = filtersets.RequisicaoFilterSet

