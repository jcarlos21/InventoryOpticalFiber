from netbox.views import generic
from . import forms, models, tables


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
    queryset = models.TipoBobina.objects.all()
    table = tables.TipoBobinaTable

class TipoBobinaEditView(generic.ObjectEditView):
    queryset = models.TipoBobina.objects.all()
    form = forms.TipoBobinaForm

class TipoBobinaDeleteView(generic.ObjectEditView):
    queryset = models.TipoBobina.objects.all()

# Bobina

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

# Requisicao

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