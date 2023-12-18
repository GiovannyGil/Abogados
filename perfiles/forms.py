# forms.py
from django import forms
from .models import Perfil
from django.contrib.auth.models import User  # Importa la clase User desde Django


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia', 'image']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
