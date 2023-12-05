from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
# Serializers
from .serializers import Operadoras_Serializer
from utils.database import searchPostgres
from rest_framework.renderers import JSONRenderer
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class GetAllOperadora(viewsets.GenericViewSet):

    @swagger_auto_schema(
        operation_description="Obtiene información de las operadoras.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos de operadoras",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de la operadora"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre de la operadora"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos para las operadoras",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description="vacio"),
                    },
                ),
            ),
        },
    )
    @action(detail=False, methods=['get'])
    def getOperadora(self, request):

        query = f"SELECT distinct id_operadora,nombre FROM administrativo.operadoras;"

        acceso = searchPostgres(query)
        # Convierte ReturnList en una lista de Python
        python_list = [Operadoras_Serializer(
            instance).data for instance in acceso]
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