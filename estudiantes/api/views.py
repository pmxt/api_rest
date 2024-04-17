from rest_framework import viewsets
from estudiantes.models import lista, pago
from estudiantes.api.serializer import PagoSerializer, ListaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = pago.objects.all()
    serializer_class = PagoSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    serializer_class = ListaSerializer
