from django import forms
from .models import *


class habitacionform(forms.ModelForm):
    class Meta:
        model = Habitacion # Nombre modelo de Habitacion
        # Campos que se van a mostrar en el formulario
        fields = '__all__'