from django.shortcuts import render, redirect

# Create your views here.



from app.persona.models import Persona, Cliente, Empleado

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from app.persona.forms import PersonaForm, EmpleadoForm, CLienteForm    
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from app.persona.filters import ClienteFilter



# Create your views here.



class EmpleadoList(ListView):
    model = Empleado
    template_name = 'empleado/empleado_list.html'
    paginate_by = 10


class EmpleadoCrear(CreateView):
    model = Empleado
    second_model = Persona
    template_name = 'empleado/empleado_form.html'
    form_class = EmpleadoForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('sueldo_crear')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoCrear, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            empleado = form.save(commit=False)
            empleado.persona = form2.save()
            empleado.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class DeleteEmpleado(DeleteView):
    model = Empleado
    template_name = 'empleado/eliminar_empleado.html'
    success_url= reverse_lazy('empleado_listar')

class UpdateEmpleado(UpdateView):
    model= Empleado
    second_model= Persona
    template_name = 'empleado/empleado_form.html'
    form_class = EmpleadoForm
    second_form_class= PersonaForm
    success_url= reverse_lazy('empleado_listar')

    def get_context_data(self, **kwargs):
        context = super(UpdateEmpleado, self).get_context_data(**kwargs)
        pk= self.kwargs.get('pk',0)        
        empleado = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=empleado.persona_id)
        

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id']=pk
        
        return context
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_empleado = kwargs['pk']
        empleado = self.model.objects.get(id=id_empleado)
        persona = self.second_model.objects.get(id=empleado.persona_id)
        form = self.form_class(request.POST, instance=empleado)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())







class ClienteListar(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    paginate_by = 10


class ClienteCrear(CreateView):
    model = Cliente
    second_model = Persona
    template_name = 'cliente/cliente_form.html'
    form_class = CLienteForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('listar_venta')

    def get_context_data(self, **kwargs):
        context = super(ClienteCrear, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            empleado = form.save(commit=False)
            empleado.persona = form2.save()
            empleado.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


def personasListar(request):  
    if request.GET:        
        if (request.GET.get('persona__nombres') and request.GET.get('persona__nombres')) is not "":                       
            cliente = Cliente.objects.all()
            filtro = ClienteFilter(request.GET, queryset=cliente)            
            return render(request, 'filtros/filtroPersonas.html', {'filtro': filtro})
        else:
            cliente = Cliente.objects.none()
            filtro = ClienteFilter(request.GET, queryset=cliente)
            return render(request, 'filtros/filtroPersonas.html', {'filtro': filtro})
    else:
        cliente = Cliente.objects.none()
        filtro = ClienteFilter(request.GET, queryset=cliente)
        return render(request, 'filtros/filtroPersonas.html', {'filtro': filtro})


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_eliminar.html'
    success_url = reverse_lazy('cliente_listar')

class ClienteUpdate(UpdateView):
    model = Cliente
    second_model = Persona
    template_name = 'cliente/cliente_form.html'
    form_class = CLienteForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('cliente_listar')

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cliente = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=cliente.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_cliente = kwargs['pk']
        cliente = self.model.objects.get(id=id_cliente)
        persona = self.second_model.objects.get(id=cliente.persona_id)
        form = self.form_class(request.POST, instance=cliente)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
