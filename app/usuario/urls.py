from django.urls import path, include

from app.usuario.views import RegistroUsuario
from django.contrib.auth.views import LoginView


# agregamos la vista index de mascota para poder usar


urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name='registrar'),    
]
