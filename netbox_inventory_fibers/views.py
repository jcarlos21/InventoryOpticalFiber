from netbox.views import generic
from . import forms, models, tables
from django.db.models import Count

# Fornecedor:

# Detail View (Exibição de detalhes)
class FornecedorView(generic.ObjectView):
    queryset = models.Fornecedor.objects.all()

# List view (Exibição de lista)
class FornecedorListView(generic.ObjectListView):
    queryset = models.Fornecedor.objects.all()
    table = tables.FornecedorTable

# Edit view (Exibição de edição)
class FornecedorEditView(generic.ObjectEditView):
    queryset = models.Fornecedor.objects.all()
    form = forms.FornecedorForm

# Delete view (Exibição de exclusão)
class FornecedorDeleteView(generic.ObjectEditView):
    queryset = models.Fornecedor.objects.all()

# TipoBobina:

class TipoBobinaView(generic.ObjectView):
    queryset = models.TipoBobina.objects.all()

class TipoBobinaListView(generic.ObjectListView):
    queryset = models.TipoBobina.objects.annotate(
        bobina_count=Count('bobinas')
    )
    table = tables.TipoBobinaTable

class TipoBobinaEditView(generic.ObjectEditView):
    queryset = models.TipoBobina.objects.all()
    form = forms.TipoBobinaForm

class TipoBobinaDeleteView(generic.ObjectEditView):
    queryset = models.TipoBobina.objects.all()

# Bobina:

class BobinaView(generic.ObjectView):
    queryset = models.Bobina.objects.all()

class BobinaListView(generic.ObjectListView):
    queryset = models.Bobina.objects.all()
    table = tables.BobinaTable

class BobinaEditView(generic.ObjectEditView):
    queryset = models.Bobina.objects.all()
    form = forms.BobinaForm

class BobinaDeleteView(generic.ObjectEditView):
    queryset = models.Bobina.objects.all()

# Requisicao:
class RequisicaoView(generic.ObjectView):
    queryset = models.Requisicao.objects.all()

class RequisicaoListView(generic.ObjectListView):
    queryset = models.Requisicao.objects.all()
    table = tables.RequisicaoTable

class RequisicaoEditView(generic.ObjectEditView):
    queryset = models.Requisicao.objects.all()
    form = forms.RequisicaoForm

class RequisicaoDeleteView(generic.ObjectEditView):
    queryset = models.Requisicao.objects.all()