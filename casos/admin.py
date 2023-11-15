from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Caso)
admin.site.register(models.TipoCaso)