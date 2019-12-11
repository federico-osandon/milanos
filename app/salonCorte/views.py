from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from app.salonCorte.models import Corte
from app.salonCorte.forms import CorteForm

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

 
        
            
            
       
        
