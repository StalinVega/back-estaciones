from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
# Serializers
from .serializers import Owners_Serializer
from utils.database import searchPostgres
from rest_framework.renderers import JSONRenderer
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class GetAllOwners(viewsets.GenericViewSet):
    @swagger_auto_schema(
        operation_description="Obtiene información de los propietarios.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos de propietarios",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id del propietario"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del propietario"),


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
    @action(detail=False, methods=['get'])
    def lista(self, request):
        query = f"SELECT distinct id_propietario,propietario FROM administrativo.vta_estaciones ORDER BY propietario;"

        estaciones = searchPostgres(query)
        # Convierte ReturnList en una lista de Python
        python_list = [Owners_Serializer(
            instance).data for instance in estaciones]
        data = {
            'success': True,
            'msg': 'ok',
            'data': python_list,

        }

        return Response(data, status=status.HTTP_200_OK)
