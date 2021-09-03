from django import forms
from .models import MaterialesPractica

class MaterialesForm(forms.ModelForm):
    class Meta:
        model= MaterialesPractica
        fields=['nombrePractica','hora','solicitante','grupo','material']