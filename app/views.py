from django.shortcuts import render

# funciones para carga de templates (vistas)



# funcion para  la pagina inicio
def inicio(request):
    return render(request, 'app/Publicas/inicio/inicio.html')

# funcion para  la pagina habitaciones
def habitaciones(request):
    return render(request, 'app/Publicas/habitaciones/habitaciones.html')

# funcion para  la pagina detalle habitaciones
def detalleHabitaciones(request):
    return render(request, 'app/Publicas/detalle-habitaciones/detalle-habitaciones.html')

# funcion para  la pagina servicios 
def servicios(request):
    return render(request, 'app/Publicas/servicios/servicios.html')
    
# funcion para  la pagina detalle servicios
def detalleServicios(request):
    return render(request, 'app/Publicas/detalle-servicios/detalle-servicios.html')

# funcion para  la pagina conocenos
def conocenos(request):
    return render(request, 'app/Publicas/conocenos/conocenos.html')

# funcion para  la pagina prueba
def prueba(request):
    return render(request, 'app/paginaPrueba.html')

# funcion para  la pagina reserva para todos
def reservas(request):
    return render(request, 'app/Publicas/reserva/reserva.html')

def reserva_emp(request):
    return render(request, "app/Empleados/reserva-emp/reserva-emp.html")

def perfil_empleado(request):
    return render(request, "app/Empleados/perfil-empleado/perfil-empleado.html")

def cliente_emp(request):
    return render(request, "app/Empleados/cliente-emp/cliente-emp.html")

def habitacion_emp(request):
    return render(request, "app/Empleados/habitacion-emp/habitacion-emp.html")

def perfil_usuario(request):
    return render(request, "app/Usuarios/perfil-usuario/perfil-usuario.html")

def servicio_emp(request):
    return render(request, 'app/Empleados/servicio-emp/servicio-emp.html')

