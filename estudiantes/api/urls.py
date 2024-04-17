from rest_framework.routers import DefaultRouter
from estudiantes.api.views import ListaViewSet, PagoViewSet

router = DefaultRouter()
router.register('estudiantes', ListaViewSet, basename='estudiante')
router.register('pagos', PagoViewSet, basename='pago')

urlpatterns = router.urls
