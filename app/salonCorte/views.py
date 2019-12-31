from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.salonCorte.models import Corte, Tintura, Mano
from app.salonCorte.forms import CorteForm, TinturaForm, ManoForm

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
      

class ColorEliminar(ListView):
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
