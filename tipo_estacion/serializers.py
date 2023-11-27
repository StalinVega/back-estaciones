# serializers.py
from rest_framework import serializers
from .models import tipoEstacion

class Tipos_estacion_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_tipo_estacion')  
    nombre = serializers.CharField(source='tipo_estacion')
    class Meta:
        model = tipoEstacion
        fields = ('id',
                  'nombre')
