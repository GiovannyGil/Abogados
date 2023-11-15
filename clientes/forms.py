from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = '__all__'
        fields = ['nombre', 'apellido', 'fecha_Nac', 'sexo', 'documento', 'tipo', 'NumDocumento']
