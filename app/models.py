from django.db import models


class Cliente(models.Model):
    Rut_cliente = models.CharField(max_length=10, primary_key=True)
    Pnombre_cliente = models.CharField(max_length=40)
    Snombre_cliente = models.CharField(max_length=40)
    Papellido_cliente = models.CharField(max_length=40)
    Sapellido_cliente = models.CharField(max_length=40)
    email_cliente = models.EmailField()
    telefono_cliente = models.IntegerField()
    direccion_cliente = models.CharField(max_length=100)

    def __str__(self):
        return self.Rut_cliente

        
class Empleado(models.Model):
    Rut_Empleado = models.CharField(max_length=10,primary_key=True)
    nombre_empleado = models.CharField(max_length=40)
    Papellido_Empleado = models.CharField(max_length=40)
    Sapellido_Empleado = models.CharField(max_length=40)
    email_Empleado = models.EmailField()
    telefono_Empleado = models.IntegerField()
    cargo = models.CharField(max_length=30,default='')
    direccion = models.CharField(max_length=60,default='')
    def __str__(self):
        return self.Rut_Empleado
    





class Empresa(models.Model):
    Rut_empresa = models.CharField(max_length=10, primary_key=True)
    dv_empresa = models.CharField(max_length=1)
    nombre = models.CharField(max_length=40)
    tipo_empresa = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.Rut_empresa
    



    
class Servicio_Ext(models.Model):
    n_s_ext = models.CharField(max_length=10, primary_key=True)
    descripcion_breve = models.TextField(max_length=100,default='')
    descripcions_ext = models.TextField(max_length=100)
    precios_ext = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)    
    imagen = models.ImageField(upload_to='servicios', null=True)
    def __str__(self):
        return self.n_s_ext
    




class Habitacion(models.Model):
    n_habitacion = models.CharField(max_length=10, primary_key=True)
    descripcion_breve = models.CharField(max_length=100,default='')
    descripcion = models.TextField(max_length=500)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='habitaciones', null=True)
    def __str__(self):
        return self.n_habitacion
    

    
    
class reserva(models.Model):
    id_reserva = models.IntegerField(default=0, primary_key=True)
    fechaInicio = models.DateField(default=None)
    fechaFinal = models.DateField(default=None)
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    n_s_ext = models.ForeignKey(Servicio_Ext, on_delete=models.PROTECT)
    n_habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT)
    precio_total = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.id_reserva)
    
    
class boleta(models.Model):
    id_boleta = models.CharField(max_length=10, primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    id_reserva = models.ForeignKey(reserva, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.id_boleta    
    
class pago(models.Model):
    id_pago = models.CharField(max_length=10, primary_key=True)
    monto = models.IntegerField()
    fecha = models.DateField()
    id_boleta = models.ForeignKey(boleta, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.id_pago
    

# Create your models here.
