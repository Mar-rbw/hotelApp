from django.shortcuts import render
from .models import Hotel
# Create your views here.

def hotelList(request):
    hotels = Hotel.objects.all()
    return render(request, 'hoteles/hotelList.html', {'hotels': hotels})

def hotelDetail(request, idHotel):
    hotel = Hotel.objects.get(pk=idHotel)
    return render(request, 'hoteles/hotelDetail.html',{'hotel':hotel})

