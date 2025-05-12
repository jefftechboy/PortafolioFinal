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
def reserva(request):
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

# funcion para  la pagina servicios empleado
def crear_servicios_emp(request):
    return render(request, "app/Empleados/crear-servicio-emp/crear-servicio-emp.html")
    
# funcion para la pagina crear habitacion empleado
def crear_habitacion_emp(request):
    return render(request, "app/Empleados/crear-habitacion-emp/crear-habitacion-emp.html")
# funcion para la pagina crear cliente empleado
def crear_cliente_emp(request):
    return render(request, "app/Empleados/crear-cliente-emp/crear-cliente-emp.html")
# funcion para la pagina crear reserva empleado
def crear_reserva_emp(request):
    return render(request, "app/Empleados/crear-reserva-emp/crear-reserva-emp.html")
# funcion para crear login 
def login(request):
    return render(request, "app/Login/login.html")
# funcion para confirmar reserva
def confirmar_reserva(request):
    return render(request, "app/Publicas/confirmacion-reserva/confirmacion-reserva.html")