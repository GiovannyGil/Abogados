from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cita, TipoCita
from .forms import CitaForm
from clientes.models import Cliente

# importar los usuarios
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url="/login/")
def citas(request):
    getCitas = Cita.objects.all()
    return render(request, "citas/index.html", {"citas": getCitas})


@login_required(login_url="/login/")
def AddCita(request):
    # llamar a los usuarios
    usuarios = User.objects.all()
    # llamar a los clientes
    clientes = Cliente.objects.all()
    # llamar a los tipos de citas
    tipos = TipoCita.objects.all()

    if request.method == "POST":
        try:
            form = CitaForm(request.POST)
            cita = form.save(commit=False)

            # verificar la cantidad de clientes seleccionados
            id_clientes = request.POST.getlist("id_cliente")

            if len(id_clientes) > 1:
                cita.save()
                # relacion muchos a muchos con clientes
                for cliente_id in id_clientes:
                    cita.id_cliente.add(cliente_id)
            else:
                cita.save()
                cita.id_cliente.add(id_clientes[0])
            return redirect("citas")
        except ValueError:
            return render(
                request,
                "citas/AddCita.html",
                {
                    "form": CitaForm,
                    "error": "Por Favor Verifica los datos",
                    "usuarios": usuarios,
                    "clientes": clientes,
                    "tipos": tipos,
                },
            )
    else:
        return render(
            request,
            "citas/AddCita.html",
            {
                "form": CitaForm,
                "usuarios": usuarios,
                "clientes": clientes,
                "tipos": tipos,
            },
        )


@login_required(login_url="/login/")
def CitaDetail(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    # relacion muchos a muchos con clientes, obtener los clientes de la cita
    clientes = cita.id_cliente.all()
    return render(
        request, "citas/DetailCita.html", {"cita": cita, "clientes": clientes}
    )


@login_required(login_url="/login/")
def CitaRemove(request, pk):
    cita = get_object_or_404(Cita, id=pk)
    cita.delete()
    return redirect("citas")


@login_required(login_url="/login/")
def CitaUpdate(request, pk):
    # llamar a los usuarios
    usuarios = User.objects.all()
    # llamar a los clientes
    clientes = Cliente.objects.all()
    # llamar a los tipos de citas
    tipos = TipoCita.objects.all()
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == "POST":
        try:
            form = CitaForm(request.POST, instance=cita)
            if form.is_valid():
                form.save()
                return redirect("citas")
        except ValueError:
            return render(
                request,
                "citas/UpdateCita.html",
                {
                    "form": CitaForm,
                    "error": "Por Favor Verifica los datos",
                    "usuarios": usuarios,
                    "clientes": clientes,
                    "tipos": tipos,
                },
            )
    else:
        form = CitaForm(instance=cita)
    return render(
        request,
        "citas/UpdateCita.html",
        {
            "form": form,
            "cita": cita,
            "usuarios": usuarios,
            "clientes": clientes,
            "tipos": tipos,
        },
    )
