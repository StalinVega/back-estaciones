from django.db import models
# Create your models here.

class estadoEstacion(models.Model):
    id_estado_estacion=models.IntegerField(blank=True)
    estado_estacion=models.CharField()
    
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
