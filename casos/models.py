from django.db import models

# importar modelo de clientes
from clientes.models import Cliente

# Create your models here.


# clase -> tabla = para el tipo de casos
class TipoCaso(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


# clase para los documentos

# -----


# clase -> tabla = para los casos
class Caso(models.Model):  # tabla para los casos
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(
        max_length=100, null=False, blank=False
    )  # titulo del caso
    descripcion = models.CharField(
        max_length=50, null=False, blank=False
    )  # descripcion del caso
    tipo = models.ForeignKey(
        TipoCaso, on_delete=models.CASCADE, null=False, blank=False
    )
    # relacion con tipo de caso
    # cliente, una relacion de muchos a muchos, un cliente puede tener muchos casos
    id_cliente = models.ManyToManyField(Cliente, verbose_name="Cliente", blank=False)
    #    TipoAbogado = models.ManyToManyField(TipoAbogado, verbose_name='Tipo_Abogado', blank=False)

    documentos = models.FileField(
        upload_to="documentos/casos", null=True, blank=True
    )  # campo para subir documentos, foreingkey -> ya que se puede necesitar varios documentos
    estado = models.BooleanField(
        default=False, blank=False, null=False
    )  # estado del caso, default false, para pendiente

    def __str__(self):
        return self.titulo