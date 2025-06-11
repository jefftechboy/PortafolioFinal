from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.utils.dateparse import parse_date
from datetime import datetime
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout

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







# VISTA SERVICIOS
def servicios(request):
    return render(request, 'app/Publicas/servicios/servicios.html')
# VISTA SERVICIOS
def detalle_servicios(request):
    return render(request, 'app/Publicas/detalle-servicios/detalle-servicios.html', data)

# VISTA AGENDA
def agenda(request):
    return render(request, "app/Empleados/agenda/agenda.html")


""" --------------------------------- CRUD COMPLETADOS --------------------------------- """
def crear_usuario(request):

    return render(request, "app/Usuarios/perfil-usuario/crear_perfil_usuario.html", data)
""" -------- PERFIL EXISTENTES ------ """
# VISTA PERFIL USUARIO






def perfil_usuario(request, id):
    try:
        cliente = Cliente.objects.get(Rut_cliente=id)
    except Cliente.DoesNotExist:
        return redirect('crear_usuario', id=id)  # Usa el name correcto de tu URL

    reserv = reserva.objects.filter(rut_cliente=id)
    data = {
        'reservas': reserv,
        'clientes': ClienteForm(instance=cliente),
        'datos': "Listado"
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Perfil actualizado correctamente"
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al actualizar el perfil"

    return render(request, "app/Usuarios/perfil-usuario/perfil-usuario.html", data)


def crear_usuario(request, id):
    data = {
        'form': ClienteForm(initial={
                'Rut_cliente': id,  # o cliente.id si es una FK
                'email_cliente': request.user.email
            }),    
    }
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    return render(request, 'app/Usuarios/perfil-usuario/crear_perfil_usuario.html', data)










# VISTA PERFIL USUARIO
def editar_perfil_usuario(request, id):
    reserv = reserva.objects.filter(rut_cliente=id)
    cliente = Cliente.objects.get(Rut_cliente=id)
    data = {
        'reservas': reserv,
        'clientes': ClienteForm(instance=cliente),
        'datos': "Editar"

    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="perfil_usuario",id=cliente.Rut_cliente)
        else:
            data["form"] = formulario
    return render(request, "app/Usuarios/perfil-usuario/perfil-usuario.html", data)

# ---------- ELIMINAR
def eliminar_perfil_usuario(request, id):
    cliente = Cliente.objects.filter(Rut_cliente=id)
    cliente.delete()
    return redirect(to="inicio")












"""" RESERVAS CLIENTES """
    # VISTA RESERVAS
def reservas(request, id):
    cliente = Cliente.objects.get(Rut_cliente=id)

    now = datetime.now()
    identificador = now.strftime("%Y%m%d%H%M%S") + now.strftime("%f")[:3]

    data = {
        'form': ReservaForm(initial={'rut_cliente': id}),
        'clienteInfo': cliente,
        'identificador': identificador,
    }

    if request.method == 'POST':
        formulario = ReservaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formfinal = formulario.save(commit=False)
            formfinal.rut_cliente = cliente

            # Fechas
            fecha_inicio = formulario.cleaned_data['fechaInicio']
            fecha_final = formulario.cleaned_data['fechaFinal']
            diferencia_dias = (fecha_final - fecha_inicio).days

            # Obtener objeto habitación y servicio
            n_habitacion = formulario.cleaned_data['n_habitacion']
            serv = formulario.cleaned_data['n_s_ext']

            # Buscar precio de habitación
            precio_habitacion = 0
            habitacion_obj = None
            if hasattr(n_habitacion, 'pk'):
                habitacion_obj = n_habitacion
            else:
                habitacion_obj = Habitacion.objects.filter(pk=n_habitacion).first()
            if habitacion_obj:
                precio_habitacion = habitacion_obj.precio

            # Buscar precio servicio
            precio_servicio = 0
            servicio_obj = None
            if hasattr(serv, 'pk'):
                servicio_obj = serv
            else:
                servicio_obj = Servicio_Ext.objects.filter(pk=serv).first()
            if servicio_obj:
                precio_servicio = servicio_obj.precios_ext

            # Calcular total
            total_calculado = diferencia_dias * precio_habitacion + precio_servicio * diferencia_dias
            if(total_calculado<0):
                data = {
                    'error_fecha': "Dia fecha invalida",
                    'form': ReservaForm(initial={'rut_cliente': id}),
                    'clienteInfo': cliente,
                    'identificador': identificador,
                }
                return render(request, 'app/Publicas/reserva/reservas.html', data)
                
            
            datos_reserva = {
                'rut_cliente': formulario.cleaned_data['rut_cliente'],
                'id_reserva': formulario.cleaned_data['id_reserva'],
                'fechaInicio': fecha_inicio,
                'fechaFinal': fecha_final,
                'dias_diferencia': diferencia_dias,
                'serv': serv,
                'n_habitacion': n_habitacion,
                'servicios': Servicio_Ext.objects.all(),
                'habitaciones': Habitacion.objects.all(),
                'total_calculado': total_calculado,
                'form': ReservaForm(),
            }
            if request.method == 'POST':
                formulario = ReservaForm(request.POST, request.FILES)
                if formulario.is_valid():
                    formfinal = formulario.save(commit=False)  # esto te da el modelo
                    formfinal.precio_total = total_calculado   # aquí asignas el valor correcto
                    formfinal.save()
            data['mensaje'] = "Reserva creada correctamente"
            return render(request, "app/Publicas/confirmacion-reserva/confirmacion-reserva.html", datos_reserva)
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




""" REGISTRO DE USUARIOS """
def registro_usuario(request):
    data = {
        'form': UserRegisterForm()
    }
    if request.method == 'POST':
        formulario = UserRegisterForm(data = request.POST)
        if formulario.is_valid():
            user = formulario.save()

             # Agregar al grupo "Clientes"
            grupo_clientes, creado = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo_clientes)


            user = authenticate(
                username=formulario.cleaned_data['username'], 
                password=formulario.cleaned_data['password1']
            )
            login(request, user)
            
            return redirect(to="inicio")
        else:
            data['form'] = formulario
            data['mensaje'] = "Error al crear el usuario"
    return render(request, "registration/registro.html",data)


def enviar_correo(request):
    enviado = False
    error = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        if nombre and email and mensaje:
            mensaje_completo = f"Mensaje de {nombre} ({email}):\n\n{mensaje}"
            try:
                send_mail(
                    'Nuevo mensaje de contacto',
                    mensaje_completo,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                enviado = True
            except Exception as e:
                error = str(e)
        else:
            error = "Por favor complete todos los campos."

    return render(request, 'app/Empleados/listar_reservas_emp.html', {
        'enviado': enviado,
        'error': error,
    })