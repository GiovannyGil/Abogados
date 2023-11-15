from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.



class TipoAbogado(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, unique=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Tipo de Abogado'
        verbose_name_plural = 'Tipos de Abogados'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    #user = models.OneToOneField('auth.User', on_delete=models.CASCADE) # relaciona el perfil con el usuario
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='perfil') # relaciona el perfil con el usuario
    image = models.ImageField(default='users/default.png', upload_to='users/') # imagen de perfil
    TipoAbogado = models.ManyToManyField(TipoAbogado, verbose_name='Tipo_Abogado', blank=False) # relaciona el perfil con el tipo de abogado
    biografia = models.TextField(max_length=500, blank=True, null=True) # biografia del abogado
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']
        
    def __str__(self):
        return self.user.username
    




def createUserProfile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance) # crea un perfil para el usuario creado
def SaveUserProfile(sender, instance, **kwargs):
    instance.perfil.save() # guarda el perfil del usuario creado

post_save.connect(createUserProfile, sender=User) # crea un perfil para el usuario creado
post_save.connect(SaveUserProfile, sender=User) # guarda el perfil del usuario creado