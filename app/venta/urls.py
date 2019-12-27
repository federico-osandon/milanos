from django.urls import path, include
from app.venta.views import VentaList, VentaCrear, VentaListar, HistorialCliente, PagoList, VentaUpdate, VentaDelete, SueldoCreate, SueldoPagar, AdelantoIng, UpdateView, SueldoUpdate
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url




urlpatterns = [
    path('listar', login_required(VentaList.as_view()), name='venta_listar'),
    path('editar/<pk>/', login_required(VentaUpdate.as_view()), name='venta_editar'),
    path('eliminar/<pk>/', login_required(VentaDelete.as_view()), name='venta_eliminar'),
    path('crear/<pk>/', login_required(VentaCrear.as_view()), name='venta_crear'),
    path('listar1', login_required(VentaListar.as_view()), name='listar_venta'),
    path('historial/<pk>/', login_required(HistorialCliente.as_view()), name='cliente_historial'),
    path('pago/<pk>/', login_required(PagoList.as_view()), name='pago_empleado'),
    path('sueldo', login_required(SueldoCreate.as_view()), name='sueldo_crear'),
    path('sueldomodificar/<int:pk>/', login_required(SueldoUpdate.as_view()), name='sueldo_modificar'),
    path('pagar/<int:pk>/', login_required(SueldoPagar), name='sueldo_pagar'),
    path('adelantoing/<int:pk>/', login_required(views.AdelantoIng), name='adelanto_ingresar'),
    
]
