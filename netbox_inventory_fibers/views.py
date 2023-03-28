from netbox.views import generic
from . import forms, models, tables, filtersets
from django.db.models import Count

# Fornecedor:

# Detail View (Exibição de detalhes)
class FornecedorView(generic.ObjectView):
    queryset = models.Fornecedor.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.BobinaTable(instance.bobinas_to_fornecedor.all())
        table.configure(request)
        return {
            'bobinas_table': table
        }

# List view (Exibição de lista)
class FornecedorListView(generic.ObjectListView):
    queryset = models.Fornecedor.objects.annotate(
        bobinas_associadas=Count('bobinas_to_fornecedor')
    )
    table = tables.FornecedorTable
    filterset = filtersets.FornecedorFilterSet
    filterset_form = forms.FornecedorFilterForm
    
# Edit view (Exibição de edição)
class FornecedorEditView(generic.ObjectEditView):
    queryset = models.Fornecedor.objects.all()
    form = forms.FornecedorForm

# Delete view (Exibição de exclusão)
class FornecedorDeleteView(generic.ObjectDeleteView):
    queryset = models.Fornecedor.objects.all()

# TipoBobina:

class TipoBobinaView(generic.ObjectView):
    queryset = models.TipoBobina.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.BobinaTable(instance.bobinas.all())
        table.configure(request)
        return {
            'tipo_bobinas_table': table
        }

class TipoBobinaListView(generic.ObjectListView):
    queryset = models.TipoBobina.objects.annotate(
        bobinas_associadas=Count('bobinas')  # deve ser igual ao que aparece na model 'Bobina', em "related_name='bobinas'"
    )
    table = tables.TipoBobinaTable

class TipoBobinaEditView(generic.ObjectEditView):
    queryset = models.TipoBobina.objects.all()
    form = forms.TipoBobinaForm

class TipoBobinaDeleteView(generic.ObjectDeleteView):
    queryset = models.TipoBobina.objects.all()

# Quantidade de fibras no cabo

class QuantidadeFibraCaboView(generic.ObjectView):
    queryset = models.QuantidadeFibraCabo.objects.all()

class QuantidadeFibraCaboListView(generic.ObjectListView):
    queryset = models.QuantidadeFibraCabo.objects.annotate(
        bobinas_associadas=Count('bobinas_to_quantidade')
    )
    table = tables.QuantidadeFibraCaboTable

class QuantidadeFibraCaboEditView(generic.ObjectEditView):
    queryset = models.QuantidadeFibraCabo.objects.all()
    form = forms.QuantidadeFibraCaboForm

class QuantidadeFibraCaboDeleteView(generic.ObjectDeleteView):
    queryset = models.QuantidadeFibraCabo.objects.all()

# Bobina:

class BobinaView(generic.ObjectView):
    queryset = models.Bobina.objects.all()

class BobinaListView(generic.ObjectListView):
    queryset = models.Bobina.objects.all()
    table = tables.BobinaTable
    # FilterSets
    filterset = filtersets.BobinaFilterSet
    filterset_form = forms.BobinaFilterForm

class BobinaEditView(generic.ObjectEditView):
    queryset = models.Bobina.objects.all()
    form = forms.BobinaForm

class BobinaDeleteView(generic.ObjectDeleteView):
    queryset = models.Bobina.objects.all()

# Requisicao:
class RequisicaoView(generic.ObjectView):
    queryset = models.Requisicao.objects.all()

class RequisicaoListView(generic.ObjectListView):
    queryset = models.Requisicao.objects.all()
    table = tables.RequisicaoTable
    filterset = filtersets.RequisicaoFilterSet
    filterset_form = forms.RequisicaoFilterForm

class RequisicaoEditView(generic.ObjectEditView):
    queryset = models.Requisicao.objects.all()
    form = forms.RequisicaoForm

class RequisicaoDeleteView(generic.ObjectDeleteView):
    queryset = models.Requisicao.objects.all()

# Fibra Requisitada

class FibraRequisitadaView(generic.ObjectView):
    queryset = models.FibraRequisitada.objects.all()

class FibraRequisitadaListView(generic.ObjectListView):
    queryset = models.FibraRequisitada.objects.all()
    table = tables.FibraRequisitadaTable

class FibraRequisitadaEditView(generic.ObjectEditView):
    queryset = models.FibraRequisitada.objects.all()
    form = forms.FibraRequisitadaForm

class FibraRequisitadaDeleteView(generic.ObjectDeleteView):
    queryset = models.FibraRequisitada.objects.all()