from django.shortcuts import render, redirect, get_object_or_404
from .forms import habitacionform
from .models import Habitacion
# funciones para carga de templates (vistas)from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio_Ext
from .forms import ServicioExtForm


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



def perfil_usuario(request):
    return render(request, "app/Usuarios/perfil-usuario/perfil-usuario.html")


def servicio_emp(request):
    return render(request, 'app/Empleados/servicio-emp/servicio-emp.html')


# funcion para  la pagina servicios empleado
def crear_servicios_emp(request):
    return render(request, "app/Empleados/crear-servicio-emp/crear-servicio-emp.html")
    



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

def agenda(request):
    return render(request, "app/Empleados/agenda/agenda.html")






#  --------------------------------------- --------------------- HABITACION EMPLEADOS  
# ------------------------------ Pagina habitacion empleado 
def habitacion_emp(request):
    return render(request, "app/Empleados/habitacion-emp/habitacion-emp.html")
# -------------- ----------------------------------- CRUD HABITACION EMPLEADO 
# ---------- IR A PAGINA CREAR HABITACION EMPLEADO
def visCrearHabitacionEmp(request):
    return render(request, "app/Empleados/crear-habitacion-emp/crear-habitacion-emp.html")
# ---------- CREAR HABITACION EMPLEADO
def crear_habitacion_emp(request):
    # Variable llamada data que contiene el formulario
    data = {
        'form': habitacionform()
    }
    if request.method == 'POST':
        formulario = habitacionform(data=request.POST,files=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Habitación creada correctamente"
            # Redirigir a la lista de habitaciones
            return redirect(to="listar_habitacion_emp") #Nombre de la url a la que redirige
        else:
            data["form"] = formulario
            data["mensaje"] = "Error al crear la habitación"
    return render(request, "app/Empleados/crear-habitacion-emp/crear-habitacion-emp.html",data)




# ---------- CREAR + LISTAR
def listar_habitacion_emp(request):
    data = {
        'form': habitacionform(),
        'Habitaciones': Habitacion.objects.all()
    }
    if request.method == 'POST':
        formulario = habitacionform(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Habitación creada correctamente"
            return render(request, "app/Empleados/habitacion-emp/habitacion-emp.html", data)
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al crear la habitación"     
    return render(request, "app/Empleados/habitacion-emp/habitacion-emp.html", data)
# ---------- MODIFICAR
def modificar_habitacion_emp(request, id):
    habitacion = Habitacion.objects.get(n_habitacion=id)
    data = {
        'form': habitacionform(instance=habitacion),
        'Habitaciones': Habitacion.objects.all()
    }
    if request.method == 'POST':
        formulario = habitacionform(data=request.POST, instance=habitacion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_habitacion_emp")
        else:
            data["form"] = formulario
    return render(request, "app/Empleados/habitacion-emp/habitacion-emp.html", data)
# ---------- ELIMINAR
def eliminar_habitacion_emp(request, id):
    habitacion = Habitacion.objects.get(n_habitacion=id)
    habitacion.delete()
    return redirect(to="listar_habitacion_emp")





# Crear servicio externo
def listar_servicio(request):
    data = {
        'form': ServicioExtForm(),
        'servicio': Servicio_Ext.objects.all()
    }
    if request.method == 'POST':
        formulario = ServicioExtForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Servicio creado correctamente"
            return render(request, "app/Empleados/crear-servicio-emp/crear-servicio-emp.html", data)
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al crear la habitación"
    return render(request, "app/Empleados/crear-servicio-emp/crear-servicio-emp.html", data)

# Modificar servicio externo

def modificar_servicio_ext(request, id):
    servicio = Servicio_Ext.objects.get(n_s_ext=id)
    data = {
        'form': ServicioExtForm(instance=servicio),
        'servicio': servicio.objects.all()
    }
    if request.method == 'POST':
        formulario = ServicioExtForm(data=request.POST, instance= servicio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_servicio")
        else:
            data["form"] = formulario
    return render(request, "app/Empleados/crear-servicio-emp/crear-servicio-emp.html", data)



# Eliminar servicio externo
def eliminar_servicio_ext(request, id):
    servicio = Servicio_Ext.objects.get(n_s_ext=id)
    servicio.delete()
    return redirect(to="listar_servicio_emp")


# Listar servicios externos

# Vista para el template principal servicio-emp.html
def servicio_emp_view(request):
    servicios_ext = Servicio_Ext.objects.select_related('empresa').all()  # Traemos servicios con la empresa relacionada
    return render(request, 'app/servicio-emp.html', {'servicios_ext': servicios_ext})
