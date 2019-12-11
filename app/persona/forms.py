from django import forms
from app.persona.models import Empleado, Persona, Cliente


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'fecha_nacimiento',            
            'email',
            'telefono',
        ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha de Nacimiento',            
            'email': 'Email',
            'telefono': 'Teléfono',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),           
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmpleadoForm (forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'dni',
            'direccion',        
            'titulo',
        ]
        labels = {
            'dni': 'DNI',
            'direccion': 'Dirección',
            'titulo': 'Titulo',
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class CLienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'vip',
        ]
        labels = {
            'vip':'Cliente Vip',
        }
        widgets = {
            'vip': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
