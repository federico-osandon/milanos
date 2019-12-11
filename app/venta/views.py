from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from app.venta.models import Venta, Sueldo
from app.venta.forms import VentaForm, SueldoForm

from app.persona.models import Cliente, Empleado, Persona
from django.utils.timezone import datetime
from app.salonCorte.models import Corte, Tintura, Mano, Cabina






# Create your views here.


#def get_context_data(self, **kwargs):
#        context = super(CorteCrear, self).get_context_data(**kwargs)
#        cortes = self.model.objects.get()
#        if 'form' not in context:
#            context['form'] = self.form_class(cortes)
#        return context

class VentaList(ListView):
    model = Venta
    template_name = 'venta/ventaList_nueva.html'
    paginate_by = 10

class VentaUpdate(UpdateView):
    model = Venta
    
    form_class = VentaForm
    template_name = 'venta/venta_update.html'
    success_url = reverse_lazy('listar_venta')

    

    def post(self, request, *args, **kwargs):
        
        precioTintura = 0
        precioCorte = 0
        precioMano = 0
        precioCabina = 0
        
        self.object = self.get_object
        pk = self.kwargs['pk']
        venta = self.model.objects.get(id=pk)
        print(venta.cliente)
        
        
        form = self.form_class(request.POST, instance=venta)
        
        post = form.save(commit=False)
        
        
        

        if post.tintura is not None:
            tintura = Tintura.objects.get(nombre=post.tintura)
            precioTintura = tintura.precio
        if post.corte is not None:
            corte = Corte.objects.get(nombre=post.corte)
            precioCorte = corte.precio
        if post.mano is not None:
            mano = Mano.objects.get(concepto=post.mano)
            precioMano = mano.precio
        if post.cabina is not None:
            cabina = Cabina.objects.get(concepto=post.cabina)
            precioCabina = cabina.precio
        if post.tipoPago is not None:
            if post.tipoPago == "Credito":
                post.total = precioTintura + precioCorte + precioMano + precioCabina + \
                    (((precioTintura + precioCorte + precioMano + precioCabina) * 5) / 100)
            if post.tipoPago == 'Cuenta':
                post.total = precioTintura + precioCorte + precioMano + precioCabina + \
                    ((precioTintura + precioCorte +
                      precioMano + precioCabina) * 10) / 100
            if (post.tipoPago == 'Debito') or (post.tipoPago == 'Efectivo'):
                post.total = precioTintura + precioCorte + precioMano + precioCabina
        else:
            post.total = precioTintura + precioCorte + precioMano + precioCabina
        post.pagoPeluquero = (((precioTintura + precioCorte) * 65) / 100)
        post.pagoPeluqueroCalculo = post.pagoPeluquero
        if form.is_valid():
            solicitud = form.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.HttpResponseRedirect(self.get_context_data(form=form))


class VentaDelete(DeleteView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_delete.html'
    success_url = reverse_lazy('listar_venta')


class VentaCrear(CreateView, ListView):
  
    model = Venta
    form_class = VentaForm
    second_model = Cliente
    template_name = 'venta/ventaList.html'
    success_url = reverse_lazy('listar_venta')
    #paginate_by= 2
    ordering = ['id']
    
    def get_context_data(self , **kwargs):
       context = super(VentaCrear, self).get_context_data(**kwargs)
       pk = self.kwargs.get('pk', 0)
       cliente = self.second_model.objects.get(id=pk)
       #data = {'cliente': cliente}
       form = self.form_class()
       context['cliente']=cliente       
       #context['form'] = self.form_class()
       context['form'] = form
       return context
       
    def get_queryset(self, **kwargs):
        queryset = super(VentaCrear, self).get_queryset()
        fecha = datetime.now()
        pk = self.kwargs.get('pk', 0)
        cliente = self.second_model.objects.get(id=pk)       
        if self.request.GET.get('fecha'):            
            fecha_str = self.request.GET.get('fecha')
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
        return queryset.filter(fecha=fecha)

    
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', 0)
        cliente = self.second_model.objects.get(id=pk)        
        precioTintura = 0
        precioCorte = 0
        precioMano = 0
        precioCabina = 0        
        self.object = self.get_object        
        form = self.form_class(request.POST)
        post = form.save(commit=False)
        post.cliente = cliente
                
        if post.tintura is not None:            
            tintura = Tintura.objects.get(nombre=post.tintura)
            precioTintura = tintura.precio
        if post.corte is not None:            
            corte = Corte.objects.get(nombre=post.corte)            
            precioCorte = corte.precio        
        if post.mano is not None:            
            mano = Mano.objects.get(concepto=post.mano)            
            precioMano = mano.precio
        if post.cabina is not None:            
            cabina = Cabina.objects.get(concepto=post.cabina)            
            precioCabina = cabina.precio    
        if post.tipoPago is not None:
            if post.tipoPago == "Credito":                
                post.total = precioTintura + precioCorte + precioMano + precioCabina + (((precioTintura + precioCorte+ precioMano + precioCabina ) * 5) / 100)
            if post.tipoPago == 'Cuenta':
                post.total = precioTintura + precioCorte + precioMano + precioCabina + ((precioTintura + precioCorte + precioMano + precioCabina) * 10) / 100                
            if (post.tipoPago == 'Debito') or (post.tipoPago == 'Efectivo'):
                post.total = precioTintura + precioCorte + precioMano + precioCabina            
        else:            
            post.total = precioTintura + precioCorte + precioMano + precioCabina 
        post.pagoPeluquero = (((precioTintura + precioCorte) * 65) / 100)
        post.pagoPeluqueroCalculo = post.pagoPeluquero
        if form.is_valid():
            solicitud = form.save()            
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class VentaListar(ListView):
    model = Venta
    form_class = VentaForm
    second_model = Cliente
    template_name = 'venta/ventaList_nueva.html'
    success_url = reverse_lazy('listar_venta')
    #paginate_by= 2
    ordering = ['id'] 
    
    def get_queryset(self, **kwargs):
        queryset = super(VentaListar, self).get_queryset()
        fecha = datetime.now() 
        if self.request.GET.get('fecha'):
            fecha_str = self.request.GET.get('fecha')
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
        return queryset.filter(fecha=fecha)

class HistorialCliente(ListView):
    model = Venta
    template_name = 'venta/historial_cliente.html'
    paginate_by = 10

    def get_queryset(self, **kwargs):
        queryset = super(HistorialCliente, self).get_queryset()
        pk = self.kwargs.get('pk', 0)       
        return queryset.filter(cliente=pk)


class PagoList(ListView):
    model = Sueldo
    second_model= Venta
    template_name = 'empleado/sueldo.html'
    paginate_by = 10
    
    def get_queryset(self, **kwargs):
        queryset = super(PagoList, self).get_queryset()
        pk = self.kwargs.get('pk', 0)
        sueldo= self.model.objects.get(peluquero= pk)
        ventas = self.second_model.objects.all()
        #print(sueldo.peluquero)
        
        pago = 0
        for venta in ventas:            
            if (venta.peluquero == sueldo.peluquero) and (venta.pagoPeluqueroCalculo != 0):                
                pago = pago + venta.pagoPeluqueroCalculo                
                venta.save()                    
        sueldo.pago_semanal = pago - sueldo.adelanto        
        sueldo.save()
        return queryset.filter(peluquero=pk)

    



class SueldoCreate(CreateView):
    model = Sueldo
    form_class = SueldoForm
    template_name = 'empleado/sueldo_form.html'
    success_url = reverse_lazy('empleado_listar')

    
     

def SueldoPagar(request, pk):    
    sueldo = Sueldo.objects.get(id=pk)   
    ventas = Venta.objects.all()
    for venta in ventas:
        if (venta.peluquero == sueldo.peluquero) and (venta.pagoPeluqueroCalculo != 0):
            venta.pagoPeluqueroCalculo = 0
            venta.save()
    sueldo.pago_semanal = 0    
    sueldo.adelanto = 0
    sueldo.save()
    peticion = request.META.get('HTTP_REFERER') 
    return redirect(peticion)






#def AdelantoIng(request, pk):
#    peticion = request.META.get('HTTP_REFERER')
#    return redirect(request)
    

def AdelantoIng(request, pk):
    if request.method == 'GET':
        adelantoForm = request.GET['ade']
        sueldo = Sueldo.objects.get(id=pk)
        
        sueldo.adelanto = sueldo.adelanto + float(adelantoForm)
        sueldo.pago_semanal = sueldo.pago_semanal - sueldo.adelanto
        print(sueldo.pago_semanal)
        sueldo.save()
        
        return redirect(request.META.get('HTTP_REFERER'))
        



