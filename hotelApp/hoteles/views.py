from django.shortcuts import render, redirect
from hoteles.models import Hotel
from hoteles.forms import HotelForm
# Create your views here.

def listaHotel(request):
    hoteles = Hotel.objects.all()
    return render(request, 'hoteles/listaHotel.html', {'hoteles': hoteles})

def crearHotel(request):
    form = HotelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaHotel')
    return render(request, 'hoteles/crearHotel.html', {'form':form})

def editarHotel(request, id):
    hotel = Hotel.objects.get(id=id)
    form = HotelForm(request.POST or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('listaHotel')
    return render(request,'hoteles/editarHotel.html', {'form':form, 'hotel':hotel })

def eliminarHotel(request,id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('listaHotel')