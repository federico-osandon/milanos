from django.contrib import admin
from app.salonCorte.models import Corte, Color, Tintura, Mano, Cabina 

# Register your models here.

admin.site.register(Corte)
admin.site.register(Color)
admin.site.register(Tintura)
admin.site.register(Mano)
admin.site.register(Cabina)