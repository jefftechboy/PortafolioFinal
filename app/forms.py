from django import forms
from .models import *


class habitacionform(forms.ModelForm):
    class Meta:
        model = Habitacion # Nombre modelo de Habitacion
        # Campos que se van a mostrar en el formulario
        fields = '__all__'
        
class ServicioExtForm(forms.ModelForm):
    class Meta:
        model = Servicio_Ext
        fields = '__all__'        




# forms.py
class ReservaForm(forms.ModelForm):
    class Meta:
        model = reserva
        fields = '__all__'
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'type': 'date'}),
            'fechaFinal': forms.DateInput(attrs={'type': 'date'}),
        }


   

        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente 
        
        fields = '__all__'
        

