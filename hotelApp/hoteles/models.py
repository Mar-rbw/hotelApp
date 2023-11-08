from django.db import models

# Create your models here.

class Hotel(models.Model):
    nombreHotel = models.CharField(max_length=20)
    direccionHotel = models.CharField(max_length=30)
    habitacionHotel = models.IntegerField()
    tarifaHotel = models.FloatField()
    fonoHotel = models.CharField(max_length=15)
    mascotaHotel = models.CharField(max_length=5)
    numeroHotel = models.IntegerField()

    def __str__(self):
        return self.nombreHotel
    