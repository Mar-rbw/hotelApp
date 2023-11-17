from django.shortcuts import render

# Create your views here.
def prueba(request):
    p = 10
    render(request, 'habitacionApp/habitacionApp.html', p)