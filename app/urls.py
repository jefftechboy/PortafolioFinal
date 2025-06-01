from django.urls import path

# importacion de las vistas
from .views import *

# Declaracion de url de navegacion para la aplicacion
urlpatterns = [
    # Pagina de inicio
    path("", inicio, name="inicio"),
    # Pagina de Conocenos
    path("conocenos/", conocenos, name="conocenos"),
    #Pagina para login
    path("login/", login, name="login"),


# ---------------------------------------------------- CRUD   ! PENDIENTES ¡ -------------------------------------------------
    # Para la pagina de confirmacion de reserva
    path("confirmar-reserva/", confirmar_reserva, name="confirmar_reserva"),
    # Pagina de perfil usuario
    path("perfil_usuario/", perfil_usuario, name="perfil_usuario"),
    # Para la pagina de agenda de la empresa
    path("agenda/", listar_agenda_emp, name= "agenda"),


    

# ---------------------------------------------------- CREATE READ UPDATE DELETE  -------------------------------------------------
    # RESERVA CLIENTES
    path("reservas/<id>/", reservas, name="reservas"),

    # INFORMACION DE SERVICIOS GENERALES
    path("informacion_servicios/", informacion_servicios, name="informacion_servicios"),
    # INFORMACION DE SERVICIOS A DETALLE
    path("detalle_servicios/<id>/", detalle_servicios, name="detalle_servicios"),

    # INFORMACION DE HABITACION DE DETALLES
    path("detalle_Habitaciones/<id>/", detalle_Habitaciones, name="detalle_Habitaciones"),
    # INFORMACION HABITACIONES 
    path("informacion_habitaciones/", informacion_habitaciones, name="informacion_habitaciones"),
    # INFORMACION HABITACIONES DETALLE
    path("detalle_Habitaciones/", detalle_Habitaciones, name="detalle_Habitaciones"),
    # PERFIL EMPLEADO
    path("listar_empleado/<id>/", listar_empleado, name="listar_empleado"),



    # HABITACION EMPLEADO
    path("listar_habitacion_emp/", listar_habitacion_emp, name="listar_habitacion_emp"),
    path("modificar_habitacion_emp/<id>/", modificar_habitacion_emp, name="modificar_habitacion_emp"),
    path("eliminar_habitacion_emp/<id>/", eliminar_habitacion_emp, name="eliminar_habitacion_emp"),

    # SERVICIO EMPLEADO
    path("listar_servicio/", listar_servicio, name="listar_servicio"),
    path("modificar_servicio_ext/<id>/", modificar_servicio_ext, name="modificar_servicio_ext"),
    path("eliminar_servicio_ext/<id>/", eliminar_servicio_ext, name="eliminar_servicio_ext"),

    # CLIENTE EMPLEADO
    path("listar_cliente_emp/", listar_cliente_emp, name="listar_cliente_emp"),
    path("modificar_cliente_emp/<id>/", modificar_cliente_emp, name="modificar_cliente_emp"),
    path("eliminar_cliente_emp/<id>/", eliminar_cliente_emp, name="eliminar_cliente_emp"),

    # RESERVA EMPLEADO
    path("listar_reservas_emp/", listar_reservas_emp, name="listar_reservas_emp"),
    path("modificar_reserva_emp/<id>/", modificar_reserva_emp, name="modificar_reserva_emp"),
    path("eliminar_reserva_emp/<id>/", eliminar_reserva_emp, name="eliminar_reserva_emp"),







    
] 