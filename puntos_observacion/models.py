from django.db import models
# Create your models here.
class PuntoObservacion(models.Model):
    id_punto_obs=models.IntegerField(blank=True)
    codigo = models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name



class PuntoObservacionBusqueda(models.Model):
    id_punto_obs=models.IntegerField(blank=True)
    id_acceso=models.IntegerField(blank=True)
    id_metodo_acceso=models.IntegerField(blank=True)
    id_cuenca=models.IntegerField(blank=True)
    id_provincia=models.IntegerField(blank=True)
    id_canton=models.IntegerField(blank=True)
    id_parroquia=models.IntegerField(blank=True)
    codigo = models.CharField(max_length=50)
    punto_obs =models.CharField(max_length=50)
    propietario=models.IntegerField(blank=True)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
class insertarPuntoObs(models.Model):
    id_punto_obs= models.IntegerField(blank=True)
    id_cuenca= models.IntegerField(blank=True)
    id_parroquia= models.IntegerField(blank=True)
    id_acceso= models.IntegerField(blank=True)
    id_metodo_acceso= models.IntegerField(blank=True)
    codigo= models.CharField()
    nombre= models.CharField()
    direccion= models.CharField()
    estado= models.BooleanField()
    us_ingreso= models.CharField()
    fecha_ingreso= models.CharField()
    us_modificacion= models.CharField()
    fecha_modificacion= models.CharField()
    referencia= models.CharField()



    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.puntos_observacion'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    

