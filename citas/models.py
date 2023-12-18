from django.db import models
from clientes.models import Cliente
from django.contrib.auth.models import User

# Create your models here.
# tabla de tipo citas


class TipoCita(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Cita(models.Model):
    id = models.BigAutoField(primary_key=True)
    Nombre_Persona = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateTimeField("Fecha cita")
    motivo = models.CharField(max_length=100)  # motivo de la cita
    Descripcion = models.TextField(max_length=200)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE,
    # null=False, blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # relacion con tabla usuarios, eliminacion en cascada

    tipo = models.ForeignKey(
        TipoCita, on_delete=models.CASCADE)
    id_cliente = models.ManyToManyField(Cliente, verbose_name="Cliente")

    def __str__(self):
        return self.Nombre_Persona
