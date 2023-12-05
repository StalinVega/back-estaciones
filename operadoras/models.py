from django.db import models
# Create your models here.
    
class Operadoras(models.Model):
    id_operadora=models.IntegerField()
    nombre= models.CharField()
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.operadoras'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    