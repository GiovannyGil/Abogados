from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cita
from .forms import CitaForm

# Create your views here.


@login_required(login_url='/login/')
def citas(request):
    getCitas = Cita.objects.all()
    return render(request, "citas/index.html", {'citas': getCitas})


@login_required(login_url='/login/')
def AddCita(request):
    if request.method == 'POST':
        try:
            form = CitaForm(request.POST)
            cita = form.save(commit=False)
            cita.save()
            return redirect("citas")
        except ValueError:
            return render(
                request,
                "citas/AddCita.html",
                {"form": CitaForm, "error": "Por Favor Verifica los datos"},
            )
    else:
        return render(
                request,
                "citas/AddCita.html",
                {"form": CitaForm, "error": "ALGO SALIO MAL"},
            )


@login_required(login_url='/login/')
def CitaDetail(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, "citas/DetailCita.html", {'cita': cita})


@login_required(login_url='/login/')
def CitaRemove(request, pk):
    cita = get_object_or_404(Cita, id=pk)
    cita.delete()
    return redirect("citas")


@login_required(login_url='/login/')
def CitaUpdate(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/UpdateCita.html',
                  {'form': form,
                   'cita': cita})
