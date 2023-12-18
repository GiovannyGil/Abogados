from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Caso, TipoCaso
from .forms import CasoForm
from clientes.models import Cliente
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url="/login/")
def casos(request):
    getCasos = Caso.objects.all()
    # SELECT * FROM Caso => traer todos lo registros de la tabla caso
    return render(request, "casos/index.html", {"casos": getCasos})
    # renderizar la vista index.html y pasarle los casos


@login_required(login_url="/login/")
def AddCaso(request):
    clientes = Cliente.objects.all()
    tipos = TipoCaso.objects.all()

    if request.method == "POST":
        try:
            form = CasoForm(request.POST)
            caso = form.save(commit=False)
            if "documentos" in request.FILES:
                # Verifica si se envió un documento
                caso.documentos = request.FILES[
                    "documentos"
                ]  # Asigna la documento al campo 'documento'

            #  verificar la cantidad de clientes seleccionados
            id_clientes = request.POST.getlist("id_cliente")

            if len(id_clientes) > 1:
                caso.save()
                # relacion muchos a muchos con clientes
                for cliente_id in id_clientes:
                    caso.id_cliente.add(cliente_id)
            else:
                caso.save()
                caso.id_cliente.add(id_clientes[0])
            return redirect("casos")
        except ValueError:
            return render(
                request,
                "casos/AddCaso.html",
                {
                    "form": CasoForm,
                    "error": "Por Favor Verifica los datos",
                    "clientes": clientes,
                    "tipos": tipos,
                },
            )
    else:
        return render(
            request,
            "casos/AddCaso.html",
            {
                "form": CasoForm,
                "error": "Por Favor Verifica los datos",
                "clientes": clientes,
                "tipos": tipos,
            },
        )


@login_required(login_url="/login/")
def CasoDetail(request, pk):
    caso = get_object_or_404(Caso, pk=pk)
    return render(request, "casos/DetailCaso.html", {"caso": caso})


@login_required(login_url="/login/")
def CasoRemove(request, pk):
    caso = get_object_or_404(Caso, id=pk)
    caso.delete()
    return redirect("casos")


@login_required(login_url="/login/")
def CasoUpdate(request, pk):
    caso = get_object_or_404(Caso, pk=pk)
    clientes = Cliente.objects.all()
    tipos = TipoCaso.objects.all()

    try:
        if request.method == "POST":
            form = CasoForm(request.POST, instance=caso)
            if form.is_valid():
                form.save()
                return redirect("casos")
        else:
            form = CasoForm(instance=caso)
        return render(
            request,
            "casos/UpdateCaso.html",
            {"form": form, "caso": caso, "clientes": clientes, "tipos": tipos},
        )
    except ValueError:
        return render(
            request,
            "casos/UpdateCaso.html",
            {
                "form": CasoForm,
                "error": "Por Favor Verifica los datos",
                "clientes": clientes,
                "tipos": tipos,
            },
        )
