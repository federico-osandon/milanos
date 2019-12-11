from django.contrib import admin
from app.persona.models import Cliente, Empleado, Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Empleado)

