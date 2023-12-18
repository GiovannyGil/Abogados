from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from perfiles.forms import UserForm, UserProfileForm
from .models import Perfil, TipoAbogado

# from .forms import UserProfileForm, UserFormn
# Create your views here.


# Create your views here.
@login_required(login_url="/login/")
def perfil(request):
    Tipo = TipoAbogado.objects.all()
    # usuario = Perfil.objects.all()
    usuario = request.user
    return render(request, "perfiles/index.html",
                  {"usuario": usuario,
                   "tipo": Tipo})


# # funcion para agregar un nuevo usuario
# def UpdateUsuario(request, pk):
#     tipo = TipoAbogado.objects.all()
#     usuario = get_object_or_404(Perfil, pk=pk)
#     try:
#         if request.method == "POST":
#             form = UserForm(request.POST, instance=usuario)
#             if form.is_valid():
#                 form.save()
#                 print("Actualizado con Exito 1")
#                 return redirect("perfiles/index.html",)
#             print("Actualizado con Exito 2")
#         else:
#             form = UserForm(instance=usuario)
#             errores = form.errors
#             print("ALGO SALIO MAL", errores)
#         return render(
#             request,
#             "perfiles/index.html",
#             {"form": form, "usuario": usuario,
#              "tipo": tipo,
#              "error": "No se Pudo ACTUALIZAR el Usuario"},
#             print("No se Pudo ACTUALIZAR el Usuario")
#         )
#     except ValueError:
#         return render(
#             request,
#             "perfiles/index.html",
#             {"form": UserProfileForm,
#              "error": "No se Pudo ACTUALIZAR el Usuario"},
#             print("ERROR FATAL AL ACTUALIZAR", ValueError),
#         )
