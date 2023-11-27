# serializers.py
from rest_framework import serializers
from .models import Accesos,Metodos_Acceso

class Accesos_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_acceso')  
    nombre = serializers.CharField(source='nombre_acceso')
    class Meta:
        model = Accesos
        fields = ('id',
                  'nombre')
        
class Metodos_Accesos_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_metodo_acceso')  
    nombre = serializers.CharField(source='nombre_metodo_acceso')
    class Meta:
        model = Metodos_Acceso
        fields = ('id',
                  'nombre')
