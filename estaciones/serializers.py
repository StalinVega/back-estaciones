# serializers.py
from rest_framework import serializers
from .models import Estaciones



class Estaciones_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_estacion')  
    nombre = serializers.CharField(source='punto_obs')
    class Meta:
        model = Estaciones
        fields = ('id',
                  'nombre')
        

class Estaciones_id_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_estacion')
    idPuntoObservacion = serializers.IntegerField(source='id_punto_obs')
    idPropietario = serializers.IntegerField(source='propietario')
    idTipoCaptor = serializers.IntegerField(source='id_captor')
    nombre = serializers.CharField(source='punto_obs')
    imgNorte = serializers.CharField(source='img_norte')
    imgSur = serializers.CharField(source='img_sur')
    imgEste = serializers.CharField(source='img_este')
    imgOeste = serializers.CharField(source='img_oeste')
    imgCroquis = serializers.CharField(source='croquis')

    class Meta:
        model = Estaciones
        fields = ('id',
                  'idPuntoObservacion',
                  'idPropietario',
                  'idTipoCaptor',
                  'nombre',
                  'imgNorte',
                  'imgSur',
                  'imgEste',
                  'imgOeste',
                  'imgCroquis')
        

