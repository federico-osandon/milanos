from django import forms
from app.venta.models import Venta, Sueldo

class VentaForm(forms.ModelForm):    
    class Meta:
        model= Venta        
        fields = [
            'peluquero',            
            'corte',
            'tintura',
            'mano',
            'cabina',
            'tipoPago',
            'fecha',
            
        ]
        labels = {
            'peluquero':'Peluqueros',
            'cliente':'',
            'corte':'Tipo de Cortes',
            'tintura': 'Colores',
            'mano':'Belleza de manos',
            'cabina':'Cabina Solar',
            'tipoPago':'Tipo de Pago',
            'fecha':'',
            'pagoPeluquero':'',
            'pagoPeluqueroCalcular':'',
            'total':'',
        }
        widgets = {
            'peluquero': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'corte': forms.Select(attrs={'class': 'form-control', 'require': 'false'}),
            'tintura': forms.Select(attrs={'class': 'form-control', 'require': 'false'}),
            'mano': forms.Select(attrs={'class': 'form-control', 'require': 'false'}), 
            'cabina': forms.Select(attrs={'class': 'form-control', 'require': 'false'}), 
            'tipoPago': forms.Select(attrs={'class': 'form-control', 'require': 'false'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'require': 'false', 'readonly':'readonly'}),
            'pagoPeluquero': forms.NumberInput(attrs={'class': 'form-control', 'require': 'false'}),
            'pagoPeluqueroCalcular': forms.NumberInput(attrs={'class': 'form-control', 'require': 'false'}),
            'total': forms.NumberInput(attrs={'class': 'form-control ', 'require': 'false'}),
        }

class SueldoForm(forms.ModelForm):
    class Meta:
        model = Sueldo
        fields = [
            'peluquero',
            'tipo_empleado',
            'pago_semanal',
            'sueldo_basico',
            'adelanto',
            'porcentaje',
        ]
        labels = {
            'peluquero':'Peluqueros',
            'tipo_empleado':'Tipo de Empleado',
            'pago_semanal':'Pago semanal',
            'sueldo_basico':'Sueldo Basico (opcional)',
            'adelanto':'Adelanto',
            'porcentaje':'Porcentaje de Comision',
        }
        widgets = {
            'peluquero': forms.Select(attrs={'class': 'form-control'}),
            'tipo_empleado': forms.Select(attrs={'class': 'form-control'}),
            'pago_semanal': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'sueldo_basico':forms.NumberInput(attrs={'class': 'form-control'}),
            'adelanto': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
        }






