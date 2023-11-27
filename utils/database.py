import psycopg2
import configparser
from django.db import IntegrityError

# Instantiate the configuration parser
config = configparser.ConfigParser()

# Parse an existing file
config.read('./config.ini')

class ConexionPostgres:
    def __init__(self):
        """
        Inicializa la conexión a la base de datos PostgreSQL.
        """
        self._conexion, self._cursor = conectar_postgres()

    def consulta(self, query):
        """
        Ejecuta una consulta en la base de datos PostgreSQL.

        Args:
            query (str): Consulta SQL a ejecutar.

        Returns:
            list: Resultado de la consulta en forma de lista de diccionarios.
        """
        try:
            self._cursor.execute(query)
            return self.dictfetchall(self._cursor)

        except psycopg2.Error as e:
            print("Ocurrió un error al conectar a PostgreSQL: ", e)

    def dictfetchall(self, cursor):
        """
        Convierte los resultados de una consulta en forma de cursor en una lista de diccionarios.

        Args:
            cursor (psycopg2.extensions.cursor): Cursor de la consulta.

        Returns:
            list: Resultado de la consulta en forma de lista de diccionarios.
        """
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def existe_registro(self, tabla, campo_id, valor_id):
        """
        Verifica si un registro ya existe en la base de datos.

        Args:
            tabla (str): Nombre de la tabla.
            campo_id (str): Nombre del campo ID.
            valor_id: Valor del campo ID que se va a verificar.

        Returns:
            bool: True si el registro ya existe, False de lo contrario.
        """
        query = f"SELECT COUNT(*) FROM {tabla} WHERE {campo_id} = %s"
        params = (valor_id,)
        self._cursor.execute(query, params)
        return self._cursor.fetchone()[0] > 0
    
    
    def guardar(self, query, params=None, tabla=None, campo_id=None, valor_id=None):
        """
        Guarda un registro en la base de datos.

        Args:
            query (str): Consulta SQL de inserción.
            params (tuple): Parámetros de la consulta.
            tabla (str): Nombre de la tabla.
            campo_id (str): Nombre del campo ID.
            valor_id: Valor del campo ID que se va a verificar.

        Returns:
            bool: True si la inserción fue exitosa, False de lo contrario.
        """
        if tabla and campo_id and valor_id:
            if self.existe_registro(tabla, campo_id, valor_id):
                print(f"El registro con {campo_id}={valor_id} ya existe.")
                return False

        try:
            self._cursor.execute(query, params)
            self._conexion.commit()
            return True
        except IntegrityError as e:
            print(f"Error al insertar datos: {e}")
            self._conexion.rollback()
            return False
        except Exception as e:
            print(f"Otro error: {e}")
            self._conexion.rollback()
            return False
        


    def closeConecP(self):
        """
        Cierra la conexión a la base de datos PostgreSQL.
        """
        if self._conexion is not None:
            self._conexion.close()


def conectar_postgres():
    """
    Establece una conexión con la base de datos PostgreSQL.

    Returns:
        conexion (psycopg2.extensions.connection): Conexión establecida con PostgreSQL.
        cursor (psycopg2.extensions.cursor): Cursor de la conexión.
    """
    try:
        # Obtener los valores de configuración de PostgreSQL
        user = config.get('DBPOSTGRES', 'USERNAME')
        password = config.get('DBPOSTGRES', 'PASSWORD')
        host = config.get('DBPOSTGRES', 'HOST')
        port = config.get('DBPOSTGRES', 'PORT')
        dbname = config.get('DBPOSTGRES', 'DB')

        # Establecer la conexión
        conexion = psycopg2.connect(**{
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        })
        cursor = conexion.cursor()
        return conexion, cursor
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        return None, None


def searchPostgres(query):
    """
    Executes a PostgreSQL query and returns the result as a list.

    Args:
        query (str): The PostgreSQL query to execute.

    Returns:
        list: The result of the query as a list.
    """
    basepostgres = ConexionPostgres()
    result = list(basepostgres.consulta(query))
    basepostgres.closeConecP()
    return result

def insertar(query, params=None,tabla=None, campo_id=None, valor_id=None):
    basepostgres = ConexionPostgres()
    result = basepostgres.guardar(query,params,tabla,campo_id,valor_id)
   
    
    basepostgres.closeConecP()
    return result