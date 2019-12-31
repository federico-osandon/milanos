from django.urls import path, include
from app.salonCorte.views import index, CorteListar, CorteCrear, CorteCrear, ColorCrear, ColorUpdate, ColorEliminar, ColorListar, ManoCreate, ManoList, ManoDelete, ManoUpdate
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

#from django.contrib.auth.views import

urlpatterns = [
       
    path('listarcorte', login_required(CorteListar.as_view()), name='corte_listar'),
    path('crearcorte', login_required(CorteCrear.as_view()), name='corte_crear'),
    path('listarcolor', login_required(ColorListar.as_view()), name='color_listar'),
    path('crearcolor', login_required(ColorCrear.as_view()), name='color_crear'),
    path('modificarcolor/<int:pk>/', login_required(ColorUpdate.as_view()), name='color_modificar'),
    path('eliminarcolor/<int:pk>/', login_required(ColorEliminar.as_view()), name='color_elimnar'),
    path('listarmano', login_required(ManoList.as_view()), name='mano_listar'),
    path('crearmano', login_required(ManoCreate.as_view()), name='mano_crear'),
    path('manoeliminar/<int:pk>/', login_required(ManoDelete.as_view()), name='mano_elimnar'),
    path('manomodificar/<int:pk>/', login_required(ManoUpdate.as_view()), name='mano_modificar'),


]
