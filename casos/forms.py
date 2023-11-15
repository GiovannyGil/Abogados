from django import forms
from .models import Caso

class CasoForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = '__all__'
