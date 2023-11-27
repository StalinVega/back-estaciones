from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
# Serializers
from .serializers import  estadoEstacionSerializer
from utils.database import searchPostgres
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class Lista_estado_estaciones(viewsets.GenericViewSet):

    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['GET'])
    def lista(self, request):
        if request.method == 'GET':

            query = f'''SELECT distinct id_estado_estacion,estado_estacion FROM administrativo.vta_estaciones;'''

            estaciones = searchPostgres(query)

            # Convierte ReturnList en una lista de Python
            python_list = [estadoEstacionSerializer(
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


