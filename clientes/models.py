from django.db import models


# Create your models here.
class TipoCliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.titulo


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_Nac = models.DateTimeField("Fecha Nacimiento")
    sexo = models.CharField(max_length=20)
    documento = models.FileField(
        upload_to="documentos/casos")  # cedula ...
    tipo = models.ForeignKey(
        TipoCliente, on_delete=models.CASCADE, default=0)
    NumDocumento = models.CharField(max_length=20, )

    def __str__(self):
        return self.nombre
