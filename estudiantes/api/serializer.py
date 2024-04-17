from rest_framework import serializers
from estudiantes.models import lista, pago

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lista
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = '__all__'
