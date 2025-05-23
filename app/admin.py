from django.contrib import admin
from .models import Cliente, Empleado, Empresa, Servicio_Ext, Servicio_Int, Habitacion, pais, reserva, boleta, pago
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Empresa)
admin.site.register(Servicio_Ext)
admin.site.register(Servicio_Int)
admin.site.register(Habitacion)
admin.site.register(pais)
admin.site.register(reserva)
admin.site.register(boleta)
admin.site.register(pago)
