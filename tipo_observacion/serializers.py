# serializers.py
from rest_framework import serializers
from .models import Estacion

class Tipos_observacion_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_captor')  
    nombre = serializers.CharField(source='captor')
    class Meta:
        model = Estacion
        fields = ('id',
                  'nombre')
