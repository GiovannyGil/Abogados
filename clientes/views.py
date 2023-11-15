from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm
from django.http import Http404


# Create your views here.
@login_required(login_url="/login/")
def clientes(request):
    getCliente = (
        Cliente.objects.all()
    )  # SELECT * FROM Caso => traer todos lo registros de la tabla caso
    return render(request, "clientes/index.html", {"cliente": getCliente})


def AddClientes(request):
    try:
        form = ClienteForm(request.POST)
        cliente = form.save(commit=False)
        if "documento" in request.FILES:  # Verifica si se envió un documento
            cliente.documento = request.FILES[
                "documento"
            ]  # Asigna la documento al campo 'documento'
        cliente.save()
        return redirect("clientes")
    except ValueError:
        return render(
            request,
            "clientes/AddClient.html",
            {"form": ClienteForm, "error": "Por Favor Verifica los datos"},
        )


def DetailClient(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "clientes/DetailClient.html", {"cliente": cliente})


def RemoveClient(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    cliente.delete()
    return redirect("clientes")


def UpdateClient(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/UpdateClient.html',
                  {'form': form,
                   'cliente': cliente})
