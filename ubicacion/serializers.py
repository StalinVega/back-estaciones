# serializers.py
from rest_framework import serializers
from .models import Provincia, Canton, Cuenca, Parroquia

class Provincia_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_provincia')  
    nombre = serializers.CharField(source='provincia')
    class Meta:
        model = Provincia
        fields = ('id',
                  'nombre')
        
class Canton_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_canton')  
    nombre = serializers.CharField(source='canton')
    class Meta:
        model = Canton
        fields = (
            'id',
            'nombre'
        )

class Cuenca_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_cuenca')  
    nombre = serializers.CharField(source='cuenca')
    class Meta:
        model = Cuenca
        fields = (
            'id',
            'nombre'
        )


class Parroquias_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_parroquia')  
    nombre = serializers.CharField(source='parroquia')
    class Meta:
        model = Parroquia
        fields = ('id',
                  'nombre')