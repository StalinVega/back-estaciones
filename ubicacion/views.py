from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
#Serializers
from .serializers import Provincia_Serializer,Canton_Serializer,Cuenca_Serializer,Parroquias_Serializer
from utils.database import searchPostgres
from rest_framework.renderers import JSONRenderer
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class GetAllProvince(viewsets.GenericViewSet):
             @swagger_auto_schema(
        operation_description="Obtiene la lista de todas las provincias.",
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde los datos de provincias",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de la proivincia"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre de la provincia"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos de la provincia",
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
                query = f"SELECT distinct id_provincia, provincia FROM administrativo.vta_estaciones ORDER BY provincia;"
                      
                estaciones = searchPostgres(query)
                # Convierte ReturnList en una lista de Python
                python_list = [Provincia_Serializer(instance).data for instance in estaciones]
                if len(python_list) == 0 :
                   data ={
                        'success':True,
                        'msg':'vacio',
                        'data': python_list,
                        
                        }
                else:
                        data ={
                        'success':True,
                        'msg':'ok',
                        'data': python_list,
                        
                        }
                
                return Response(data,status=status.HTTP_200_OK)


class View_Canton(viewsets.GenericViewSet):
  
    @swagger_auto_schema(
        operation_summary="Obtiene el canton",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'idProv': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Es el id de la Provincia",
                ),

            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde el listado de los cantones",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id del canton"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del canton"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos del canton",
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
    def canton(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('idProv')
            query_cantones = f'''SELECT distinct id_canton, canton 
            FROM administrativo.vta_estaciones
            Where id_provincia='{id}' ORDER BY canton;
            '''
            
            cantones = searchPostgres(query_cantones)
            
            # Convierte ReturnList en una lista de Python
            python_list = [Canton_Serializer(instance).data for instance in cantones]
           

            if len(python_list) == 0 :
                data ={
                        'success':True,
                        'msg':'vacio',
                        'data': python_list,
                        
                }
            else:
                data ={
                        'success':True,
                        'msg':'ok',
                        'data': python_list,
                        
                }
                
            return Response(data,status=status.HTTP_200_OK)
                     
                     
class View_Cuenca(viewsets.GenericViewSet):
 
    
    @swagger_auto_schema(
        operation_summary="Obtiene la Cuenca",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'idProv': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id de la provincia",
                ),
                'idCant': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id del Canton",
                ),
                'idParroq': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id de Parroquia",
                ),

            },
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(description="Responde el listado de las cuencas",
                                                 schema=openapi.Schema(
                                                     type=openapi.TYPE_ARRAY,
                                                     items=openapi.Schema(
                                                         type=openapi.TYPE_OBJECT,
                                                         properties={
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de la cuenca"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre de la cuenca"),
                                                             
                                                             
                                                         },
                                                     ),
                                                 ),),
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="No se encontraron datos de las cuencas",
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
    def post_cuenca(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            idp = data.get('idProv')
            idc = data.get('idCant')
            idpa = data.get('idParroq')
            query_cuencas = f'''SELECT distinct id_cuenca,cuenca 
            FROM administrativo.vta_estaciones 
            Where id_provincia='{idp}' and id_canton='{idc}'and id_parroquia = '{idpa}';
            '''
            
            cuencas = searchPostgres(query_cuencas)
            
            # Convierte ReturnList en una lista de Python
            python_list = [Cuenca_Serializer(instance).data for instance in cuencas]
        
            if len(python_list) == 0 :
                data ={
                        'success':True,
                        'msg':'vacio',
                        'data': python_list,
                        
                }
            else:
                data ={
                        'success':True,
                        'msg':'ok',
                        'data': python_list,
                        
                }
                
            return Response(data,status=status.HTTP_200_OK)
        
class View_Parroquia(viewsets.GenericViewSet):

    
    @swagger_auto_schema(
        operation_summary="Obtiene la Parroquia",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'idProv': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id de la provincia",
                ),
                'idCant': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="El id del Canton",
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
                                                             'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de la Parroquia"),
                                                             'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre de la Parroquia"),
                                                             
                                                             
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
    @action(detail=False, methods=['POST'])
    def parroquia(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            id_p = data.get('idProv')
            id_c = data.get('idCant')
            query_parroquia = f'''SELECT distinct id_parroquia, parroquia 
                                FROM administrativo.vta_estaciones
                                Where id_provincia='{id_p}' and id_canton='{id_c}' ORDER BY parroquia ;
            '''

            cantones = searchPostgres(query_parroquia)

            # Convierte ReturnList en una lista de Python
            python_list = [Parroquias_Serializer(
                instance).data for instance in cantones]
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