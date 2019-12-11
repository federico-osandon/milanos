from django.urls import path, include
from app.persona.views import EmpleadoList, EmpleadoCrear, ClienteListar, ClienteCrear, personasListar, DeleteEmpleado, UpdateEmpleado, ClienteDelete, ClienteUpdate
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

#from django.contrib.auth.views import

urlpatterns = [
    path('listarempleado', login_required(EmpleadoList.as_view()), name='empleado_listar'),
    path('crearempleado', login_required(EmpleadoCrear.as_view()), name='empleado_crear'),
    path('eliminarempleado/<pk>', login_required(DeleteEmpleado.as_view()), name='eliminar_empleado'),
    path('empleadoeditar/<pk>', login_required(UpdateEmpleado.as_view()), name='empleado_editar'),
    
    path('listarcliente', login_required(ClienteListar.as_view()), name='cliente_listar'),
    path('crearcliente', login_required(ClienteCrear.as_view()), name='cliente_crear'),
    path('buscar', login_required(personasListar), name='listar_persona'),
    path('clientedelete/<pk>', login_required(ClienteDelete.as_view()), name='cliente_eliminar'),
    path('clienteupdate/<pk>', login_required(ClienteUpdate.as_view()), name='cliente_editar'),
]
