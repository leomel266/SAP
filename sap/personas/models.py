import email
from django.db import models
from django.forms import CharField

# Create your models here.
class Domicilio(models.Model):
    calle= models.CharField(max_length=60)
    numero= models.IntegerField()
    pais=models.CharField(max_length=60)
    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.numero} {self.pais}'
        


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'

    