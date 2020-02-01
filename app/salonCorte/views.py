from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.salonCorte.models import Corte, Tintura, Mano, Tratamiento
from app.salonCorte.forms import CorteForm, TinturaForm, ManoForm, TratamientoForm

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

class CorteListar(ListView):
    model = Corte
    template_name = 'corte/corte_listar.html'
    paginate_by = 10


class CorteCrear(CreateView):
    model = Corte
    form_class = CorteForm
    template_name = 'corte/corte_form.html'
    success_url = reverse_lazy('corte_listar')



class CorteModificar(UpdateView):
    model = Corte
    form_class = CorteForm
    template_name = 'corte/corte_form.html'
    success_url = reverse_lazy('corte_listar')


class CorteBorrar(DeleteView):
    model = Corte    
    template_name = 'corte/corte_eliminar.html'
    success_url = reverse_lazy('corte_listar')

 
class ColorCrear(CreateView):
    model = Tintura
    form_class = TinturaForm
    template_name = 'color/color_form.html'
    success_url = reverse_lazy('color_listar')

class ColorListar(ListView):
    model = Tintura
    template_name = 'color/color_list.html'
    paginate_by = 10


class ColorUpdate(UpdateView):
    model = Tintura
    form_class = TinturaForm
    template_name = 'color/color_form.html'
    success_url = reverse_lazy('color_listar')
      

class ColorEliminar(DeleteView):
    model = Tintura
    template_name = 'color/color_delete.html'
    success_url= reverse_lazy('color_listar')
            
       
        
class ManoCreate(CreateView):
    model = Mano
    form_class = ManoForm
    template_name = 'mano/mano_form.html'
    success_url = reverse_lazy('mano_listar')
    

class ManoList(ListView):
    model = Mano
    template_name = 'mano/mano_list.html'
    paginate_by = 10


class ManoUpdate(UpdateView):
    model = Mano
    form_class = ManoForm
    template_name = 'mano/mano_form.html'
    success_url = reverse_lazy('mano_listar')


class ManoDelete(DeleteView):
    model = Mano
    template_name = 'mano/mano_delete.html'
    success_url = reverse_lazy('mano_listar')


class TratamientosListar(ListView):
    model = Tratamiento
    template_name = 'tratamiento/tratamiento_listar.html'
    paginate_by = 10


class TratamientosCrear(CreateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'tratamiento/tratamiento_form.html'
    success_url = reverse_lazy('tratamiento_listar')



class TratamientosModificar(UpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'tratamiento/tratamiento_form.html'
    success_url = reverse_lazy('tratamiento_listar')


class TratamientosBorrar(DeleteView):
    model = Tratamiento    
    template_name = 'tratamiento/tratamiento_eliminar.html'
    success_url = reverse_lazy('tratamiento_listar')
