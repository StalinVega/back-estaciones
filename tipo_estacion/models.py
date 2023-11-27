from django.db import models
# Create your models here.
class tipoEstacion(models.Model):
    id_tipo_estacion=models.IntegerField(blank=True)
    tipo_estacion = models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
