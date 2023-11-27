from django.db import models
# Create your models here.
class Provincia(models.Model):
    id_provincia=models.IntegerField(blank=True)
    provincia = models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name


class Canton(models.Model):
    id_canton=models.IntegerField(blank=True)
    canton = models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
class Cuenca(models.Model):
    id_cuenca=models.IntegerField(blank=True)
    cuenca = models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    

class Parroquia(models.Model):
    id_parroquia=models.IntegerField(blank=True)
    parroquia = models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name