from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
# importacion de las vistas

# Declaracion de url de navegacion para la aplicacion
urlpatterns = [
    # Pagina de inicio
    path("", inicio, name="inicio"),
    # Pagina de Conocenos
    path("conocenos/", conocenos, name="conocenos"),



# ---------------------------------------------------- CRUD   ! PENDIENTES ¡ -------------------------------------------------
    # Para la pagina de agenda de la empresa
    path("agenda/", listar_agenda_emp, name= "agenda"),
    
    # registro de usuario
    path("registro_usuario/", registro_usuario, name="registro_usuario"),


    path("crear_usuario/<id>/", crear_usuario, name="crear_usuario"),

    # enviar correo
    path("enviar_correo/",enviar_correo,name="enviar_correo"),






    # Paso 1: ingresar correo
    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/formularioCambioContrasena.html',
            email_template_name='registration/password_reset_email.html',
            subject_template_name='registration/password_reset_subject.txt',
            success_url='/password-reset/done/',
        ), name='password-reset'),
    # Paso 2: confirmación de que se envió el correo
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/CambioContrasenaEnviado.html'
    ), name='password_reset_done'),



    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='registration/ActualizarContrasenas.html',
    success_url='/reset/done/'
    ), name='password_reset_confirm'),




    # Paso 4: contraseña cambiada correctamente
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/CambioContrasenaCompletado.html'
    ), name='password_reset_complete'),







    path("crear_usuario/<id>/", crear_usuario, name="crear_usuario"),

# ---------------------------------------------------- CREATE READ UPDATE DELETE  -------------------------------------------------
    # Pagina de perfil usuario
    path("perfil_usuario/<id>/", perfil_usuario, name="perfil_usuario"),
    # editar perfil usuario
    path("editar_perfil_usuario/<id>/", editar_perfil_usuario, name="editar_perfil_usuario"),
    # eliminar perfil usuario
    path("eliminar_perfil_usuario/<id>/", eliminar_perfil_usuario, name="eliminar_perfil_usuario"),
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

    # RESERVACION EXITOSA
    path("registroPagoBoleta/<idReserva>/", registroPagoBoleta, name="registroPagoBoleta"),
    path("enviar_correo/", enviar_correo, name="enviar_correo"),


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