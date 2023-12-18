from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# import models de citas, casos, clientes y usuarios
from citas.models import Cita
from casos.models import Caso
from clientes.models import Cliente
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def dash(request):
    return render(request, "dash/dash.html")

'''
app para el dashboard de la pagina,
usando las citas, casos, clientes y usuarios para mostrar datos
'''

def dashboard(request):
    # Cantidad de citas
    citas = Cita.objects.all().count()
    # Cantidad de casos
    casos = Caso.objects.all().count()
    # Cantidad de clientes
    clientes = Cliente.objects.all().count()
    # Cantidad de usuarios
    usuarios = User.objects.all().count()

    return render(request, "dash/dash.html",
                  {'citas': citas,
                   'casos': casos,
                   'clientes': clientes,
                   'usuarios': usuarios
                   })
