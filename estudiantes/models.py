from django.db import models
# Create your models here.
class lista(models.Model):
    carnet = models.CharField(max_length= 20, primary_key= True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_N = models.DateField()

class pago (models.Model):
    estudiante = models.ForeignKey(lista,on_delete=models.CASCADE,to_field='carnet')
    N_boleta = models.IntegerField()
    C_banco = models.IntegerField()
    F_pago = models.DateField()