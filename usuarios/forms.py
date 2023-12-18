from django import forms
from django.contrib.auth.models import User
from perfiles.models import Perfil, TipoAbogado


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["biografia", "image"]


class UserFormClass(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
