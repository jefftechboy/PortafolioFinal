from django.urls import path

# importacion de las vistas
from .views import *

# Declaracion de url de navegacion para la aplicacion
urlpatterns = [
    # Pagina de inicio
    path("", inicio, name="inicio"),
    # Pagina de Habitacion
    path("habitaciones/", habitaciones, name="habitaciones"),
    # Pagina de Detalle habitacion
    path("detalle-habitaciones/", detalleHabitaciones, name="detalle-habitaciones"),
    # Pagina de Servicio
    # Pagina de Detalle Servicio
    path("detalle-servicios/", detalleServicios, name="detalle-servicios"),
    # Pagina de Conocenos
    path("conocenos/", conocenos, name="conocenos"),
    # Pagina de reserva para todos
    path("reserva/", reserva, name="reserva"),
    # Pagina de reserva para empleados
    path("reserva-emp/", reserva_emp, name="reserva-emp"),
    # Pagina de perfil empleado
    path("perfil-empleado/", perfil_empleado, name="perfil-empleado"),
    # Pagina de cliente empleado
    path("cliente-emp/", cliente_emp, name="cliente-emp"),



    




    
    # Pagina de perfil usuario
    path("perfil-usuario/", perfil_usuario, name="perfil-usuario"),
    # Pagina de servicio empleado
    path("servicio-emp/", servicio_emp, name="servicio_emp"),
    # Pagina de servicios empleado
    
    # Pagina de crear cliente empleado
    path("crear-cliente-emp/", crear_cliente_emp, name="crear-cliente-emp"),
    # Pagina de crear reserva empleado
    path("crear-reserva-emp/", crear_reserva_emp, name="crear-reserva-emp"),
    #Pagina para login
    path("login/", login, name="login"),
    # Para la pagina de confirmacion de reserva
    path("confirmar-reserva/", confirmar_reserva, name="confirmar-reserva"),
    # Para la pagina de confirmacion de reserva
    path("agenda/", agenda, name= "agenda"),


    # Pagina de habitacion empleado
        # Pagina habitacion empleado
            path("habitacion_emp/", habitacion_emp, name="habitacion_emp"),
        # Pagina habitacion empleado
            path("listar_habitacion_emp/", listar_habitacion_emp, name="listar_habitacion_emp"),
        # Ir al CREATE habitacion empleado
            path("crear_habitacion_emp/", crear_habitacion_emp, name="crear_habitacion_emp"),
        # Modificar habitacion empleado
            path("modificar_habitacion_emp/<id>/", modificar_habitacion_emp, name="modificar_habitacion_emp"),
        # Eliminar habitacion empleado
            path("eliminar_habitacion_emp/<id>/", eliminar_habitacion_emp, name="eliminar_habitacion_emp"),
    # Pagina de cliente empleado

    # Pagina de habitacion empleado
            path("listar_servicio/", listar_servicio, name="listar_servicio"),
            path("modificar_servicio_ext/<id>/", modificar_servicio_ext, name="modificar_servicio_ext"),
            path("eliminar_servicio_ext/<id>/", eliminar_servicio_ext, name="eliminar_servicio_ext"),
        # Modificar habitacion empleado

            # CLIENTE EMP
            path("listar_cliente_emp/", listar_cliente_emp, name="listar_cliente_emp"),
            path("modificar_cliente_emp/<id>/", modificar_cliente_emp, name="modificar_cliente_emp"),
            path("eliminar_cliente_emp/<id>/", eliminar_cliente_emp, name="eliminar_cliente_emp"),
      
       



            path("listar_reservas_emp/", listar_reservas_emp, name="listar_reservas_emp"),
            path("modificar_reserva_emp/<id>/", modificar_reserva_emp, name="modificar_reserva_emp"),
            path("eliminar_reserva_emp/<id>/", eliminar_reserva_emp, name="eliminar_reserva_emp"),
] 