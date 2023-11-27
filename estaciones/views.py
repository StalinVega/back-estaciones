from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
from .models import Estaciones
# Serializers
from .serializers import  Estaciones_Serializer,Estaciones_id_Serializer
from utils.database import searchPostgres
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class Lista_Estaciones(viewsets.GenericViewSet):

    # GET
    @swagger_auto_schema(auto_schema=None)
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

    # POST
    @swagger_auto_schema(auto_schema=None)
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
    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, pk=None):
        try:
            # Recupera el producto desde la base de datos usando el ID proporcionado
            query = f"SELECT distinct id_estacion,id_punto_obs,propietario,id_captor,punto_obs,img_norte,img_sur,img_este,img_oeste,croquis FROM administrativo.vta_estaciones where id_estacion='{pk}';"
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
