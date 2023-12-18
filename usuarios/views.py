from django.shortcuts import render, redirect, get_object_or_404  # renderizar plantillas
# importar los usuarios
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test  # permisos
from .forms import UserProfileForm, UserFormClass  # importar los formularios

def usuarios(request):
    usuarios = User.objects.all()
    # traer los roles de los usuarios
    for usuario in usuarios:
        if usuario.is_superuser:
            usuario.rol = "Administrador"
        elif usuario.is_staff:
            usuario.rol = "Staff"
        else:
            usuario.rol = "Usuario"

    return render(request, "usuarios/index.html", {"usuarios": usuarios})


# Decorador para asegurarse de que el usuario actual no sea admin ni staff
def user_is_not_admin_or_staff(user):
    # si no es admin ni staff
    return not user.is_staff and not user.is_superuser


# funcion para crear un nuevo usuario
def NewUsuario(request):
    # si el usuario no es admin ni staff
    if user_is_not_admin_or_staff(request.user):
        # mostrar mensaje de error
        return render(
            request,
            "usuarios/index.html",
            {"mensaje": "No tienes permisos para crear usuarios"},
        )
    else:
        # si el metodo es POST
        if request.method == "POST":
            # obtener los datos del formulario
            form = UserFormClass(request.POST)
            # si el formulario es valido
            if form.is_valid():
                # guardar el usuario
                form.save()
                # mostrar mensaje de exito
                return redirect("usuarios")
            else:
                # mostrar mensaje de error
                return render(
                    request,
                    "usuarios/NewUsuario.html",
                    {"mensaje": "No se ha podido crear el usuario"},
                )
        else:
            # mostrar el formulario
            form = UserFormClass()
            return render(request, "usuarios/NewUsuario.html", {"form": form})


# funcion para eliminar un usuario
def RemoveUsuario(request, id):
    try:
        # obtener el usuario
        usuario = User.objects.get(id=id)
        # verificar si el usuario que desea eliminar es admin o staff
        if user_is_not_admin_or_staff(request.user):
            # mostrar mensaje de error
            return render(
                request,
                "usuarios/index.html",
                {"mensaje": "No tienes permisos para eliminar usuarios"},
            )
        else:
            # eliminar el usuario
            usuario.delete()
            # mostrar mensaje de exito
            return redirect("usuarios")
    except Exception as e:
        # mostrar mensaje de error
        return render(
            request,
            "usuarios/RemoveUsuario.html",
            {"mensaje": "No se ha podido eliminar el usuario",
             "error": e},
        )


# funcion para mostrar la informacion de un usuario
def DetailUsuario(request, id):
    usuario = User.get_object_or_404(User, id=id)
    return render(request, "usuarios/DetailUsuario.html", {"usuario": usuario})


# funcion para actualizar la informacion de un usuario
def UpdateUsuario(request, id):
    usuario = User.objects.get(id=id)

    if request.method == "POST":
        # Obtener los datos del formulario para el modelo User
        user_form = UserFormClass(request.POST, instance=usuario)
        # Obtener los datos del formulario para el modelo Perfil
        perfil_form = UserProfileForm(request.POST, request.FILES,
                                      instance=usuario.perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            # Guardar los cambios en el modelo User
            user_form.save()
            # Guardar los cambios en el modelo Perfil
            perfil_form.save()

            return redirect("usuarios")
        else:
            return render(
                request,
                "usuarios/UpdateUsuario.html",
                {
                    "mensaje": "No se ha podido actualizar el usuario",
                    "error": user_form.errors,
                    "form": user_form,
                    "perfil_form": perfil_form,
                    "usuario": usuario,
                },
            )
    else:
        # Mostrar el formulario
        user_form = UserFormClass(instance=usuario)
        perfil_form = UserProfileForm(instance=usuario.perfil)

        return render(
            request,
            "usuarios/UpdateUsuario.html",
            {
                "mensaje": "No se ha podido actualizar el usuario",
                "error": user_form.errors,
                "form": user_form,
                "perfil_form": perfil_form,
                "usuario": usuario,
            },
        )
