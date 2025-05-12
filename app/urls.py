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
    path("servicios/", servicios, name="servicios"),
    # Pagina de Detalle Servicio
    path("detalle-servicios/", detalleServicios, name="detalle-servicios"),
    # Pagina de Conocenos
    path("conocenos/", conocenos, name="conocenos"),
    # Pagina de prueba
    path("prueba/", prueba, name="prueba"),
    # Pagina de reserva para todos
    path("reserva/", reservas, name="reserva"),

    path("reserva-emp/", reserva_emp, name="reserva-emp"),
    
    path("perfil-empleado/", perfil_empleado, name="perfil-empleado"),

    path("cliente-emp/", cliente_emp, name="cliente-emp"),

    path("habitacion-emp/", habitacion_emp, name="habitacion-emp"),

    path("perfil-usuario/", perfil_usuario, name="perfil-usuario"),

    path("servicio-emp/", servicio_emp, name="servicio-emp"),
     
    


]