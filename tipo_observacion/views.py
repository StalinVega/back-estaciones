from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
# Serializers
from .serializers import Tipos_observacion_Serializer
from utils.database import searchPostgres
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


class GetAllListaObservacion(viewsets.GenericViewSet):
    @swagger_auto_schema(
        operation_description="Obtiene información de los tipos de captor.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos de los tipos de captor",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id del captor"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del captor"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos de los captor",
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
    def lista(self, request):
        query = f"SELECT distinct id_captor,captor FROM administrativo.vta_estaciones;"

        estaciones = searchPostgres(query)
        # Convierte ReturnList en una lista de Python
        python_list = [Tipos_observacion_Serializer(
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
