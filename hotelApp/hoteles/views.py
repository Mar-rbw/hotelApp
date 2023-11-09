from django.shortcuts import render, redirect
from .models import Hotel
from .forms import HotelForm
# Create your views here.

def listaHotel(request):
    hoteles = Hotel.objects.all()
    return render(request, 'hoteles/listaHotel.html', {'hoteles': hoteles})

def crearHotel(request):
    form = HotelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaHotel')
    return render(request, 'crearHotel.html', {'form':form})

def editarHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    form = HotelForm(request.Post or None)
    if form.is_valid():
        form.save()
        return redirect('listaHotel')
    return render(request, 'editarHotel.html',{'form':form, 'hotel':hotel})

def eliminarHotel(request,id):
    hotel = Hotel.objects.get(id=id)
    if request.method == 'POST':
        hotel.delete()
        return redirect('listaHotel')
    return render(request, 'eliminarHotel.html',{'hotel':hotel} )
