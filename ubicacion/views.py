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
             @swagger_auto_schema(auto_schema=None)
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
  
    #POST
    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['POST'])
    def post_canton(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            id = data.get('id')
            query_cantones = f'''SELECT distinct id_canton, canton 
            FROM administrativo.vta_estaciones
            Where id_provincia='{id}' ORDER BY canton;
            '''
            
            cantones = searchPostgres(query_cantones)
            
            # Convierte ReturnList en una lista de Python
            python_list = [Canton_Serializer(instance).data for instance in cantones]
            respuesta_personalizada = {
            "nuevo_campo1": python_list[0],
            "nuevo_campo2": python_list[1]
            }

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
 
    #POST
    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['POST'])
    def post_cuenca(self,request):
        if request.method == 'POST':
            data = json.loads(request.body)
            idp = data.get('idp')
            idc = data.get('idc')
            idpa = data.get('idpa')
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

    # POST
    @swagger_auto_schema(auto_schema=None)
    @action(detail=False, methods=['POST'])
    def post_parroquia(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            id_p = data.get('idp')
            id_c = data.get('idc')
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