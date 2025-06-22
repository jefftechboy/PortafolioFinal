from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class habitacionform(forms.ModelForm):
    class Meta:
        model = Habitacion # Nombre modelo de Habitacion
        # Campos que se van a mostrar en el formulario
        fields = '__all__'
        






class boletaform(forms.ModelForm):
    class Meta:
        model = boleta 
        
        fields = '__all__'
class pagoform(forms.ModelForm):
    class Meta:
        model = pago 
        
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
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['email_cliente'].widget.attrs['readonly'] = True
        

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_text = ''



