from django import forms
from app.salonCorte.models import Corte, Color, Tintura, Mano



class CorteForm(forms.ModelForm):
    
    class Meta:
        model = Corte
        fields = [
            'nombre',
            'decripcion',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre',
            'decripcion': 'Descripcion',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.Select( attrs={'class': 'form-control'}),
            'decripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

       #ass ColorForm(forms.ModelForm):
       #  class Meta:
       #      model = Color
       #      fields = [
       #          'color',
       #          'codigo',
       #          'marca',
       #          'gramo',
       #          'precio',
       #      ]
       #      labels = {
       #          'color': 'Color',
       #          'codigo': 'Codigo',
       #          'marca':'Marca',
       #          'gramo':'Gramos',
       #          'precio':'Precio',
       #      }


class TinturaForm(forms.ModelForm):

    class Meta:
        model = Tintura
        fields = [
            'nombre',
            'codigo',
            'marca',
            'gramo',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre',
            'codigo': 'Codigo',
            'marca': 'Marca',
            'gramo': 'Gramos',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'gramo': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ManoForm(forms.ModelForm):
    class Meta:
        model = Mano
        fields = [
            'nombre',
            'concepto',
            'precio',
        ]
        labels = {
            'nombre': 'Nombre',
            'concepto': 'Concepto',
            'precio': 'Precio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
