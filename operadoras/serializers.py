# serializers.py
from rest_framework import serializers
from .models import Operadoras

class Operadoras_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_operadora')  
    
    class Meta:
        model = Operadoras
        fields = ('id',
                  'nombre')