from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
from .models import Estaciones
# Serializers
from .serializers import Estaciones_Serializer, Estaciones_id_Serializer
from utils.database import searchPostgres
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class Lista_Estaciones(viewsets.GenericViewSet):

    # GET
    @swagger_auto_schema(
        operation_description="Obtiene información de estaciones.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos de estaciones",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de la estacion"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre de la estacion"),


                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos de las estaciones",
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

            query = f'''SELECT distinct id_estacion,punto_obs FROM administrativo.vta_estaciones ORDER BY punto_obs;'''

            estaciones = searchPostgres(query)

            # Convierte ReturnList en una lista de Python
            python_list = [Estaciones_Serializer(
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


class Busca_Estaciones(viewsets.GenericViewSet):

    
    @swagger_auto_schema(
        operation_summary="Obtiene la Estacion",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'idObs': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id del punto de observacion",
                ),
    

            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde datos de la estacion",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de la Estacion"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre de la Estacion"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos de la Estacion",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description="vacio"),
                    },
                ),
            ),
        },
    )
    @action(detail=False, methods=['POST'])
    def post_estaciones(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            idObs = data.get('idObs')

            query = f'''SELECT distinct id_estacion,punto_obs FROM administrativo.vta_estaciones 
                                where id_punto_obs='{idObs}';
                                '''

            estaciones = searchPostgres(query)

            # Convierte ReturnList en una lista de Python
            python_list = [Estaciones_Serializer(
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


class GetIdEstacion(viewsets.GenericViewSet):

    @swagger_auto_schema(
        operation_summary="Obtiene informacion de la estacion por el id de estación",
        operation_description="""

        Args:
            request (HttpRequest): The HTTP request object containing the data object.
            
            Params:
            id: 64297
            

            (debe ser de la estacion)
        """,
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description="Es el id de la estacion", type=openapi.TYPE_INTEGER),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde la informacion de una estacion en especifico",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="es el id de la estacion"),
                                                             'idPuntoObservacion': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del punto de ibservacion"),
                                                             'idPropietario': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del propietario"),
                                                             'idTipoCaptor': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del tipo de captor"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del punto de observacion"),
                                                             'imgNorte': openapi.Schema(type=openapi.TYPE_STRING, description="Es una imagen en base64"),
                                                             'imgSur': openapi.Schema(type=openapi.TYPE_STRING, description="Es una imagen en base64"),
                                                             'imgEste': openapi.Schema(type=openapi.TYPE_STRING, description="Es una imagen en base64"),
                                                             'imgOeste': openapi.Schema(type=openapi.TYPE_STRING, description="Es una imagen en base64"),
                                                             'imgCroquis': openapi.Schema(type=openapi.TYPE_STRING, description="Es una imagen en base64"),



                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos de las Parroquias",
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
    def estacion(self, request):
        pk=request.GET.get('id')
        try:
            # Recupera el producto desde la base de datos usando el ID proporcionado
            query = f"SELECT distinct id_estacion,id_punto_obs,id_propietario,id_captor,punto_obs,img_norte,img_sur,img_este,img_oeste,croquis FROM administrativo.vta_estaciones where id_estacion='{pk}';"
            po = searchPostgres(query)
        except Estaciones.DoesNotExist:
            # Si el objeto no existe, puedes manejarlo según tus necesidades
            return Response({'error': 'El punto de observación no existe'}, status=404)

        # Convierte ReturnList en una lista de Python
        python_list = [Estaciones_id_Serializer(
            instance).data for instance in po]
        data = {
            'success': True,
            'msg': 'ok',
            'data': python_list,

        }
        return Response(data, status=status.HTTP_200_OK)
