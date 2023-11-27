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

    @swagger_auto_schema(
        operation_description="Obtiene el lisado del tipo de estado de las estaciones.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos de estado de estaciones",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id del estado de estacion"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del estado de estacion"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos para el acceso",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description="vacio"),
                    },
                ),
            ),
        },
    )
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


