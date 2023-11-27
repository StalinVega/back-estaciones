# serializers.py
from rest_framework import serializers
from .models import estadoEstacion

      

class estadoEstacionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_estado_estacion')
    nombre = serializers.CharField(source='estado_estacion')

    class Meta:
        model = estadoEstacion
        fields = ('id',
                 'nombre')
        

