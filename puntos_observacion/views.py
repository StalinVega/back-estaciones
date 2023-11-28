from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
from .models import PuntoObservacion
# Serializers
from .serializers import Punto_Observacion_Serializer, Punto_Observacion_id_Serializer
from utils.database import searchPostgres,insertar
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

class GetAllPuntoObservacion(viewsets.GenericViewSet):
    @swagger_auto_schema(
        operation_description="Obtiene información del punto de observacion.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos del punto de observacion",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id del punto de observacion"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del punto de observacion"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos del punto de oservacion",
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
        query = f"SELECT distinct id_punto_obs, codigo FROM administrativo.vta_estaciones;"

        po = searchPostgres(query)
        # Convierte ReturnList en una lista de Python
        python_list = [Punto_Observacion_Serializer(
            instance).data for instance in po]
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


class GetIdPuntoObservacion(viewsets.GenericViewSet):
    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['GET'])
    def puntoObs(self, request):
        pk=request.GET.get('id')
        try:
            # Recupera el producto desde la base de datos usando el ID proporcionado
            query = f"SELECT distinct id_punto_obs,id_acceso,id_metodo_acceso,id_cuenca,id_provincia,id_canton,id_parroquia,codigo,punto_obs,propietario FROM administrativo.vta_estaciones where id_punto_obs='{pk}';"
            po = searchPostgres(query)
        except PuntoObservacion.DoesNotExist:
            # Si el objeto no existe, puedes manejarlo según tus necesidades
            return Response({'error': 'El punto de observación no existe'}, status=404)

        # Convierte ReturnList en una lista de Python
        python_list = [Punto_Observacion_id_Serializer(
            instance).data for instance in po]
        data = {
            'success': True,
            'msg': 'ok',
            'data': python_list,

        }
        return Response(data, status=status.HTTP_200_OK)


class insertarPunto(viewsets.GenericViewSet):

    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['POST'])
    def add(self, request):
        if request.method == 'POST':

            data = json.loads(request.body)
            id_punto_obs = data.get('id_punto')
            id_cuenca = data.get('id_cuenca')
            id_parroquia = data.get('id_parroquia')
            id_acceso = data.get('id_acceso')
            id_metodo_acceso = data.get('id_metodo_acceso')
            codigo = data.get('codigo_inamhi')
            nombre = data.get('nombre_punto_obs')
            direccion = data.get('direccion')
            estado = data.get('estado')
            us_ingreso = data.get('us_ingreso')
            fecha_ingreso = data.get('fecha_ingreso')
            us_modificacion = data.get('us_modificacion')
            fecha_modificacion = data.get('fecha_modificacion')
            referencia = data.get('referencia')

            sql = f"INSERT INTO administrativo.puntos_observacion(id_punto_obs,id_cuenca, id_parroquia, id_acceso, id_metodo_acceso, codigo, nombre, direccion, estado, us_ingreso, fecha_ingreso,us_modificacion,fecha_modificacion,referencia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            data =(int(id_punto_obs),int(id_cuenca),int(id_parroquia),int(id_acceso),int(id_metodo_acceso),codigo,nombre,direccion,estado,us_ingreso,fecha_ingreso,us_modificacion,fecha_modificacion,referencia)
            ingreso = insertar(sql,data,"administrativo.puntos_observacion","id_punto_obs",id_punto_obs)
            print(ingreso)

            return Response(ingreso, status=status.HTTP_200_OK)
        

