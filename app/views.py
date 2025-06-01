from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.utils.dateparse import parse_date
from datetime import datetime

""" --------------------------------- VISTAS SIN FUNCIONES --------------------------------- """
# VISTA INICIO 
def inicio(request):
    return render(request, 'app/Publicas/inicio/inicio.html')
# VISTA CONOCENOS
def conocenos(request):
    return render(request, 'app/Publicas/conocenos/conocenos.html')


""" --------------------------------- CRUD PENDIENTES --------------------------------- """

# VISTA PERFIL EMPLEADO
def perfil_empleado(request):
    return render(request, "app/Empleados/perfil-empleado/perfil-empleado.html")
# VISTA LOGIN
def login(request):
    return render(request, "app/Login/login.html")
# VISTA CONFIRMACION RESERVA
def confirmar_reserva(request):
    return render(request, "app/Publicas/confirmacion-reserva/confirmacion-reserva.html")

# VISTA SERVICIOS
def servicios(request):
    return render(request, 'app/Publicas/servicios/servicios.html')
# VISTA SERVICIOS
def detalle_servicios(request):
    return render(request, 'app/Publicas/detalle-servicios/detalle-servicios.html', data)

# VISTA PERFIL USUARIO
def perfil_usuario(request):
    return render(request, "app/Usuarios/perfil-usuario/perfil-usuario.html")
# VISTA AGENDA
def agenda(request):
    return render(request, "app/Empleados/agenda/agenda.html")


""" --------------------------------- CRUD COMPLETADOS --------------------------------- """




"""" RESERVAS CLIENTES """
# VISTA RESERVAS


def reservas(request, id):
    cliente = Cliente.objects.get(Rut_cliente=id)

    now = datetime.now()
    # Formato con milisegundos: %f da microsegundos, tomamos los primeros 3 dígitos
    identificador = now.strftime("%Y%m%d%H%M%S") + now.strftime("%f")[:3]

    data = {
        'form': ReservaForm(initial={'rut_cliente': id}),
        'clienteInfo': cliente,
        'identificador': identificador,
    }

    if request.method == 'POST':
        formulario = ReservaForm(request.POST, request.FILES)
        if formulario.is_valid():
            # Asignar el cliente al campo rut_cliente
            formfinal = formulario.save(commit=False)
            # Asignar el identificador al campo id_reserva
            formfinal.rut_cliente = cliente  
            # Asignar el identificador al campo id_reserva
            formfinal.save()
            data['mensaje'] = "Reserva creada correctamente"
            return render(request, "app/Publicas/reserva/reservas.html", data)
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al crear la reserva"  

    return render(request, 'app/Publicas/reserva/reservas.html', data)







""" INFORMACION HABITACIONES """
def informacion_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    data = {
        'habitaciones': habitaciones
    }
    return render(request, "app/Publicas/habitaciones/habitaciones.html", data)

""" INFORMACION HABITACIONES DETALLE """
def detalle_Habitaciones(request,id):
    habitacionde = Habitacion.objects.get(n_habitacion=id)
    data = {
        'Habitaciones': habitacionde
    }
    return render(request, 'app/Publicas/detalle-habitaciones/detalle-habitaciones.html',data)


"""  INFORMACION SERVICIOS """
def informacion_servicios(request):
    servicios = Servicio_Ext.objects.all()
    data = {
        'servicios': servicios
    }
    return render(request, "app/Publicas/servicios/servicios.html", data)


""" INFORMACION SERVICIOS DETALLE """
def detalle_servicios(request,id):
    serviciode = Servicio_Ext.objects.get(n_s_ext=id)
    data = {
        'servicio': serviciode
    }
    return render(request, 'app/Publicas/detalle-servicios/detalle-servicios.html', data)




""" PERFIL EMPREADO  """
# ---------- LISTAR EMPLEADO LOGEADO
def listar_empleado(request,id):
    empleado = Empleado.objects.get(Rut_Empleado=id)
    data = {
        'empleadoDatos': empleado
    }
    return render(request, "app/Empleados/perfil-empleado/perfil-empleado.html", data)

""" HABITACION EMPLEADO """
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

""" SERVICIO EMPLEADO """
# ---------- CREAR + LISTAR
def listar_servicio(request):
    data = {
        'form': ServicioExtForm(),
        'servicios': Servicio_Ext.objects.all()
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
# ---------- MODIFICAR
def modificar_servicio_ext(request, id):
    servicio = Servicio_Ext.objects.get(n_s_ext=id)
    data = {
        'form': ServicioExtForm(instance=servicio),
        'servicios': Servicio_Ext.objects.all()
    }
    if request.method == 'POST':
        formulario = ServicioExtForm(data=request.POST, instance= servicio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_servicio")
        else:
            data["form"] = formulario
    return render(request, "app/Empleados/crear-servicio-emp/crear-servicio-emp.html", data)
# ---------- ELIMINAR
def eliminar_servicio_ext(request, id):
    servicio = Servicio_Ext.objects.get(n_s_ext=id)
    servicio.delete()
    return redirect(to="listar_servicio")

""" RESERVA EMPLEADO """
# ---------- CREAR Y LISTAR
def listar_reservas_emp(request):
    data = {
        'form': ReservaForm(),
        'reservas': reserva.objects.all()
    }
    if request.method == 'POST':
        formulario = ReservaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Reserva creada correctamente"
            data['form'] = ReservaForm()
            data['reservas'] = reserva.objects.all()  # Actualiza la lista tras crear
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al crear la reserva"
            data['reservas'] = reserva.objects.all()
    return render(request, "app/Empleados/crear-reserva-emp/crear-reserva-emp.html", data)
# ---------- MODIFICAR RESERVA
def modificar_reserva_emp(request, id):
    reservas = reserva.objects.get(id_reserva=id)  # Cambiar a tu modelo de reservas
    data = {
        'form': ReservaForm(instance=reservas),
        'reservas': reserva.objects.all()  # Cambiar a tu modelo de reservas
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reservas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_reservas_emp")
        else:
            data["form"] = formulario
    return render(request, "app/Empleados/crear-reserva-emp/crear-reserva-emp.html", data)
# ---------- ELIMINAR RESERVA
def eliminar_reserva_emp(request, id):
    reservas = reserva.objects.get(id_reserva=id)  # Cambiar a tu modelo de reservas
    reservas.delete()
    return redirect(to="listar_reservas_emp")

""" CLIENTE EMPLEADO """
# ---------- CREAR + LISTAR CLIENTE
def listar_cliente_emp(request):
    data = {
        'form': ClienteForm(),
        'clientes': Cliente.objects.all()
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Cliente creado correctamente"
            return render(request, "app/Empleados/cliente-emp/cliente-emp.html", data)
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al crear el cliente"
            data['clientes'] = Cliente.objects.all()
    return render(request, "app/Empleados/cliente-emp/cliente-emp.html", data)
# ---------- MODIFICAR CLIENTE
def modificar_cliente_emp(request, id):
    cliente = Cliente.objects.get(pk=id)
    data = {
        'form': ClienteForm(instance=cliente),
        'clientes': Cliente.objects.all()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("listar_cliente_emp")
        else:
            data["form"] = formulario
    return render(request, "app/Empleados/cliente-emp/cliente-emp.html", data)
# ---------- ELIMINAR CLIENTE
def eliminar_cliente_emp(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect("listar_cliente_emp")

""" AGENDA RESERVAS """
# ---------- LISTAR RESERVAS

def listar_agenda_emp(request):
    reservas = reserva.objects.all()

    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        fecha_inicio = parse_date(fecha_inicio)
        fecha_fin = parse_date(fecha_fin)

        if fecha_inicio and fecha_fin:

            reservas = reserva.objects.filter(
             fechaInicio__lte=fecha_fin,
             fechaFinal__gte=fecha_inicio
            )

    data = {
        'reservas': reservas
    }
    return render(request, "app/Empleados/agenda/agenda.html", data)