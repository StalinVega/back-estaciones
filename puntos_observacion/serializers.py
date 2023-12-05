# serializers.py
from rest_framework import serializers
from .models import PuntoObservacion, PuntoObservacionBusqueda, insertarPuntoObs,UltimoCodigo

class Punto_Observacion_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_punto_obs')  
    nombre = serializers.CharField(source='codigo')
    class Meta:
        model = PuntoObservacion
        fields = ('id',
                  'nombre')
        

class Punto_Observacion_id_Serializer(serializers.ModelSerializer):
    id = serializers.CharField(source='id_punto_obs')
    idAcceso = serializers.CharField(source='id_acceso')
    idMetodoAcceso = serializers.CharField(source='id_metodo_acceso')
    idCuenca = serializers.CharField(source='id_cuenca')
    idProvincia = serializers.CharField(source='id_provincia')
    idCanton =serializers.CharField(source='id_canton')
    idParroquia = serializers.CharField(source='id_parroquia')
    codigo_inamhi = serializers.CharField(source='codigo')
    nombre = serializers.CharField(source='punto_obs')
    codigoPropietaria = serializers.CharField(source='id_propietario')
    class Meta:
        model = PuntoObservacionBusqueda
        fields = ('id','idAcceso','idMetodoAcceso','idCuenca','idProvincia','idCanton','idParroquia','codigo_inamhi','nombre','codigoPropietaria')


class Punto_Observacion_Ingreso_Serializer(serializers.ModelSerializer):
    class Meta:
        model = insertarPuntoObs
        fields = '__all__'

class Ultimo_Codigo_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = UltimoCodigo
        fields = '__all__'