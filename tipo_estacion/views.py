from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
# Serializers
from .serializers import Tipos_estacion_Serializer
from utils.database import searchPostgres
from rest_framework.renderers import JSONRenderer
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


class GetAllTypeStations(viewsets.GenericViewSet):
    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['get'])
    def lista(self, request):
        query = f"SELECT distinct id_tipo_estacion,tipo_estacion from administrativo.vta_estaciones order by tipo_estacion"

        estaciones = searchPostgres(query)
        # Convierte ReturnList en una lista de Python
        python_list = [Tipos_estacion_Serializer(
            instance).data for instance in estaciones]
        if len(python_list) == 0:
            data = {
                'success': True,
                'msg': 'vacio',
                'data': python_list,

            }
        else:
            data = {
                'success': True,
                'msg': 'ok',
                'data': python_list,

            }

        return Response(data, status=status.HTTP_200_OK)
