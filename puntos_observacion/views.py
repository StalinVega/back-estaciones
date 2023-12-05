from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
from .models import PuntoObservacion
# Serializers
from .serializers import Punto_Observacion_Serializer, Punto_Observacion_id_Serializer, Ultimo_Codigo_Serializer
from utils.database import searchPostgres, insertar
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
    @swagger_auto_schema(
        operation_summary="Obtiene informacion del punto de observación por el id del mismo",
        operation_description="""

        Args:
            request (HttpRequest): The HTTP request object containing the data object.
            
            Params:
            id: 1010
            

            (debe ser del punto de observacion)
        """,
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_QUERY, description="Es el id del punto de observacion", type=openapi.TYPE_INTEGER),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde la informacion de un punto de observacion en espefico",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del punto de observacion"),
                                                             'idAcceso': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del Acceso"),
                                                             'idMetodoAcceso': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del Metodo de Acceso"),
                                                             'idCuenca': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id de la Cuenca"),
                                                             'idProvincia': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id de la Provincia"),
                                                             'idCanton': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del Canton"),
                                                             'idParroquia': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id de la Parroquia"),
                                                             'codigo_inamhi': openapi.Schema(type=openapi.TYPE_STRING, description="Es el codigo inamhi del punto de observacion"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del punto de observacion"),
                                                             'codigoPropietaria': openapi.Schema(type=openapi.TYPE_INTEGER, description="Es el id del Propietario"),



                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No existe informacion acerca del punto de observacion",
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
    def puntoObs(self, request):
        pk = request.GET.get('id')
        try:
            # Recupera el producto desde la base de datos usando el ID proporcionado
            query = f"SELECT distinct id_punto_obs,id_acceso,id_metodo_acceso,id_cuenca,id_provincia,id_canton,id_parroquia,codigo,punto_obs,id_propietario FROM administrativo.vta_estaciones where id_punto_obs='{pk}';"
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

    @swagger_auto_schema(
        operation_summary="Ingresa el Punto de Observacion",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_punto': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id del punto de observacion",
                ),
                'id_cuenca': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id de la Cuenca",
                ),
                'id_parroquia': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id de la Parroquia",
                ),
                'id_acceso': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id del Acceso",
                ),
                'id_metodo_acceso': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id del meotod de acceso",
                ),
                'codigo_inamhi': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Es el codigo inamhi del punto de observacion",
                ),
                'nombre_punto_obs': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Es el nombre del punto de observacion",
                ),
                'direccion': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Es la direccion del punto de observacion",
                ),
                'estado': openapi.Schema(
                    type=openapi.TYPE_BOOLEAN,
                    description="Es el estado de si se encuentra activa o no ese punto de observacion(True/False)",
                ),
                'us_ingreso': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Es el usuario quien hizo este ingreso",
                ),
                'fecha_ingreso': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Es la fecha que se realizo el ingreso",
                ),
                'referencia': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Es la referencia del punto de observacion",
                ),
                

            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde el listado de las parroquias",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'success': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="Es el estado de la peticion (True/False)"),
                                                             'msg': openapi.Schema(type=openapi.TYPE_STRING, description="Un mensaje de exito o error"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="Se ingreso mal el registro",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description="El registro con id_punto_obs=63814 ya existe."),
                    },
                ),
            ),
        },
    )
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
            data = (int(id_punto_obs), int(id_cuenca), int(id_parroquia), int(id_acceso), int(id_metodo_acceso), codigo,
                    nombre, direccion, estado, us_ingreso, fecha_ingreso, us_modificacion, fecha_modificacion, referencia)
            ingreso = insertar(
                sql, data, "administrativo.puntos_observacion", "id_punto_obs", id_punto_obs)
            
            if ingreso['success'] == False:
                data = {
                'success': False,
                'msg': str(ingreso['msg']),
                
                
                }
                return Response(data, status=status.HTTP_200_OK)
            else:

                data = {
                'success': True,
                'msg': 'Se Registro el punto de Observacion',
                
                }
                return Response(data, status=status.HTTP_200_OK)

            


            

            


class GetCodigo(viewsets.GenericViewSet):
    

    @swagger_auto_schema(
        operation_summary="Obtiene el ultimo codigo  más uno.",
        operation_description="""

        Args:
            request (HttpRequest): The HTTP request object containing the data object.
            
            Params:
            inicial: M o H 
            captor: MANUAL o ELECTROMECANICA

            (DEBEN ESTAR EN MAYÚSCULA)
        """,
        manual_parameters=[
            openapi.Parameter('inicial', openapi.IN_QUERY, description="Es la inicial del tipo de estacion", type=openapi.TYPE_STRING),
            openapi.Parameter('captor', openapi.IN_QUERY, description="Es el nombre del tipo de observacion", type=openapi.TYPE_STRING),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde el digito del ultimo codigo",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={

                                                             'codigo': openapi.Schema(type=openapi.TYPE_STRING, description="Es el ultimo codigo mas 1"),


                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No existe informacion",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description="verifique los datos enviados"),
                    },
                ),
            ),
        },
    )
    @action(detail=False, methods=['GET'])
    def codigo(self, request):
        inicial = request.GET.get('inicial')
        captor = request.GET.get('captor')
        
        
        if validar_sigla_tipo_estacion(inicial) and validar_tipo_captor(captor):
            query = f"SELECT captor as tipo, codigo FROM administrativo.vta_estaciones WHERE codigo = (SELECT MAX(codigo) FROM administrativo.vta_estaciones WHERE codigo LIKE '{inicial}%' AND captor = '{captor}');"

            po = searchPostgres(query)
            # Convierte ReturnList en una lista de Python
            python_list = [Ultimo_Codigo_Serializer(
                instance).data for instance in po]
            nuevoCodigo=nuevo_Codigo(python_list[0]['codigo'])
            if len(python_list) == 0:
                data = {
                'success': True,
                'msg': 'vacio',
                'data': python_list,
        

             }
            else:
            #  ingresoCodigo={'codigoN':nuevoCodigo}
            #  python_list.append(ingresoCodigo)
             data = {
                'success': True,
                'msg': 'ok',
                'data': nuevoCodigo,
                
                }

            return Response(data, status=status.HTTP_200_OK)

            
        else:
            data = {
                'success': True,
                'msg': 'verifique los datos enviados',
                'data': [],

                }
            return Response(data, status=status.HTTP_200_OK)
        
        
        

# Funciones
def validar_sigla_tipo_estacion(cadena):
    return cadena.upper() in {'M', 'H'}

def validar_tipo_captor(cadena):
    return cadena.upper() in {'MANUAL', 'ELECTROMECANICA'}

def nuevo_Codigo(cadena):
    indice_h = cadena.find('H')
    indice_m = cadena.find('M')

    # Elegir el índice más pequeño entre "H" y "M" que sea mayor que -1 (es decir, si se encuentra)
    indice_separador = min(indice_h, indice_m) if indice_h > -1 and indice_m > -1 else max(indice_h, indice_m)

    # Dividir la cadena en función del índice encontrado
    if indice_separador > -1:
        parte1 = cadena[:indice_separador]
        parte2 = cadena[indice_separador:]

        # Intentar sumar 1 a la parte numérica
        try:
            if indice_separador == indice_h:
                suma = int(parte2[1:]) + 1
                nuevo_codigo = f"{parte1}H{suma}"
                return nuevo_codigo
            elif indice_separador == indice_m:
                suma = int(parte2[1:]) + 1
                nuevo_codigo = f"{parte1}M{suma}"
                return nuevo_codigo
        except ValueError:
            # Manejar el caso en que la parte después de "H" o "M" no sea un número
            return False
    else:
        return False
