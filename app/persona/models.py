from django.db import models

# Create your models here.


class Persona(models.Model):
    nombres = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True,blank= True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']


class Empleado(models.Model):
    dni = models.CharField(max_length=15)
    direccion = models.CharField(max_length=70)
    titulo = models.BooleanField()
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.persona.nombres, self.persona.apellidos)

    class Meta:
        verbose_name = 'Empleado '
        verbose_name_plural = 'Empleados'
        ordering = ['id']


class Cliente(models.Model):
    vip = models.BooleanField()
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.persona.nombres, self.persona.apellidos)

    class Meta:
        verbose_name = 'Cliente '
        verbose_name_plural = 'Clientes'
        ordering = ['persona__apellidos']




