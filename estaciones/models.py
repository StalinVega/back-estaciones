from django.db import models
# Create your models here.


class Estaciones(models.Model):
    id_estacion=models.IntegerField(blank=True)
    id_punto_obs=models.IntegerField(blank=True)
    propietario=models.IntegerField(blank=True)
    id_captor=models.IntegerField(blank=True)
    img_norte=models.BinaryField()
    img_sur=models.BinaryField()
    img_este=models.BinaryField()
    img_oeste=models.BinaryField()
    croquis=models.BinaryField()
    punto_obs= models.CharField(max_length=50)
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
