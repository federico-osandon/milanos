from django import forms
from app.salonCorte.models import Corte, Color, Tintura



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

