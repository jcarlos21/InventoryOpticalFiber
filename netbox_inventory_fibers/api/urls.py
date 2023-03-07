from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_inventory_fibers'

router = NetBoxRouter()
router.register('fornecedor', views.FornecedorViewSet)
router.register('tipo-bobina', views.TipoBobinaViewSet)
router.register('bobina', views.BobinaViewSet)
router.register('quantidade-fibra-cabo', views.QuantidadeFibraCaboViewSet)

urlpatterns = router.urls