# serializers.py
from rest_framework import serializers
from .models import Propietario

class Owners_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='propietario')  
    nombre = serializers.CharField(source='nombre_propietario')
    class Meta:
        model = Propietario
        fields = ('id',
                  'nombre')
