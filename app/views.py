from django.shortcuts import render

# funciones para carga de templates (vistas)



# funcion para  la pagina home
def home(request):
    return render(request, 'app/home.html')

# funcion para  la pagina prueba
def prueba(request):
    return render(request, 'app/paginaPrueba.html')

# funcion para  la pagina reserva para todos
def reservas(request):
    return render(request, 'app/Publicas/reserva/reserva.html')