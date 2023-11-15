from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Perfil, TipoAbogado
# from .forms import UserProfileForm, UserFormn
# Create your views here.


# Create your views here.
@login_required(login_url="/login/")
def perfil(request):
    Tipo = TipoAbogado.objects.all()
    # usuario = Perfil.objects.all()
    usuario = request.user
    return render(request, "perfiles/index.html", {"usuario": usuario, "tipo": Tipo})
