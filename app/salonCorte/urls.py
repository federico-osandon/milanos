from django.urls import path, include
from app.salonCorte.views import index, CorteListar, CorteCrear, CorteCrear, CorteModificar, CorteBorrar,\
     ColorCrear, ColorUpdate, ColorEliminar, ColorListar, ManoCreate, ManoList, ManoDelete, ManoUpdate, \
         TratamientosListar, TratamientosCrear, TratamientosModificar, TratamientosBorrar
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

#from django.contrib.auth.views import

urlpatterns = [
       
    path('listarcorte', login_required(CorteListar.as_view()), name='corte_listar'),
    path('crearcorte', login_required(CorteCrear.as_view()), name='corte_crear'),
    path('modificarcorte/<int:pk>', login_required(CorteModificar.as_view()), name='corte_modificar'),
    path('borrarcorte/<int:pk>', login_required(CorteBorrar.as_view()), name='corte_borrar'),

    path('listarcolor', login_required(ColorListar.as_view()), name='color_listar'),
    path('crearcolor', login_required(ColorCrear.as_view()), name='color_crear'),
    path('modificarcolor/<int:pk>/', login_required(ColorUpdate.as_view()), name='color_modificar'),
    path('eliminarcolor/<int:pk>/', login_required(ColorEliminar.as_view()), name='color_elimnar'),
    
    path('listarmano', login_required(ManoList.as_view()), name='mano_listar'),
    path('crearmano', login_required(ManoCreate.as_view()), name='mano_crear'),
    path('manoeliminar/<int:pk>/', login_required(ManoDelete.as_view()), name='mano_elimnar'),
    path('manomodificar/<int:pk>/', login_required(ManoUpdate.as_view()), name='mano_modificar'),

    path('listartratamientos', login_required(TratamientosListar.as_view()), name='tratamiento_listar'),
    path('creartratamientos', login_required(TratamientosCrear.as_view()), name='tratamiento_crear'),
    path('modificartratamientos/<int:pk>', login_required(TratamientosModificar.as_view()), name='tratamiento_modificar'),
    path('borrartratamientos/<int:pk>', login_required(TratamientosBorrar.as_view()), name='tratamiento_borrar'),
]
