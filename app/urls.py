from django.urls import path

# importacion de las vistas
from .views import *

# Declaracion de url de navegacion para la aplicacion
urlpatterns = [
    # Pagina de inicio
    path("", home, name="home"),
    # Pagina de prueba
    path("prueba/", prueba, name="prueba"),
    # Pagina de reserva para todos
    path("reserva/", reservas, name="reserva"),

    path("reserva-emp/", reserva_emp, name="reserva-emp"),
    
    path("perfil-empleado/", perfil_empleado, name="perfil-empleado"),
]