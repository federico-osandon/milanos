from django.urls import path, include
from app.salonCorte.views import index, CorteListar, CorteCrear
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

#from django.contrib.auth.views import

urlpatterns = [
       
    path('listarcorte', login_required(CorteListar.as_view()), name='corte_listar'),
    path('crearcorte', login_required(CorteCrear.as_view()), name='corte_crear'),
]
