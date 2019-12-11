from django.db import models
from app.persona.models import Empleado, Cliente
from app.salonCorte.models import Corte, Tintura, Mano, Cabina
import time
from datetime import date

# Create your models here.


class Venta(models.Model):
     day = date.today()
     #day = time.strftime()
     
     TIPOPAGO_CHOICES = (('Efectivo', 'Efectivo'), ('Debito', 'Débito'), ('Credito', 'Crédito'), ('Cuenta', 'Cta. Corriente'))
     
     peluquero = models.ForeignKey(Empleado, on_delete=models.CASCADE)
     cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
     corte = models.ForeignKey(Corte, null=True,blank=True, on_delete=models.CASCADE)
     tintura = models.ForeignKey(Tintura, null=True, blank=True, on_delete=models.CASCADE)
     mano=  models.ForeignKey(Mano, null=True, blank=True, on_delete=models.CASCADE)
     cabina=  models.ForeignKey(Cabina, null=True, blank=True, on_delete=models.CASCADE)
     tipoPago = models.CharField(choices=TIPOPAGO_CHOICES,null=True,blank=True, max_length=50)
     fecha = models.DateField(default=day)
     pagoPeluquero= models.FloatField(null=True, blank=True)
     pagoPeluqueroCalculo= models.FloatField(null=True, blank=True)
     total = models.FloatField(null=True, blank=True)

     def __str__(self):
         return 'Venta {}'.format(self.id )
     

     class Meta:
          ordering= ['id']

class Sueldo(models.Model):
     TIPOEMPLEADO_CHOICES = (('Peluquero', 'Peluquero'),
                             ('Ayudante', 'Ayudante'), ('Maniquiure', 'Maniquiure'), ('Masajista', 'Masajista'))
     peluquero = models.OneToOneField(Empleado, on_delete=models.CASCADE)
     tipo_empleado = models.CharField(choices=TIPOEMPLEADO_CHOICES, null=True, blank=True, max_length=50)
     pago_semanal = models.FloatField(default=0)
     sueldo_basico = models.FloatField(null=True, blank=True, )
     adelanto = models.FloatField(default=0)
     porcentaje=models.IntegerField()

     def __str__(self):
         return 'sueldo de {}'.format(self.peluquero)     

     
     


     
