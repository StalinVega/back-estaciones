from django.db import models
# Create your models here.
    
class Accesos(models.Model):
    id_acceso=models.IntegerField(blank=True)
    nombre_acceso= models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
class Metodos_Acceso(models.Model):
    id_metodo_acceso=models.IntegerField(blank=True)
    nombre_metodo_acceso= models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name