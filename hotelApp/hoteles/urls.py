from django.urls import path
from . import views

urlpatterns = [
    path('',views.hotelList, name="hotelList"),
    path('<int:idHotel>/', views.hotelDetail, name='hotelDetail')
]
