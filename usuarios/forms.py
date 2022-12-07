from django import forms
from usuarios.models import *

class FormularioUsuarios(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese su correo electronico'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ingrese su número de celular'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'Ingrese la ciudad en la que vive'}),
            'contrasena': forms.TextInput(attrs={'type':'password','placeholder': 'Ingrese su contraseña'}),
            'imagen': forms.FileInput()
        }
