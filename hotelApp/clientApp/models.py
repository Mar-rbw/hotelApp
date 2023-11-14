from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    rutClient = models.CharField(max_length=20)
    nombreClient = models.CharField(max_length=20)
    apeliidoClint = models.CharField(max_length=20)
    fonoClient = models.CharField(max_length=30)
    llegadaClient = models.DateField()
    salidaClient = models.DateField()

    def __str__(self):
        return self.nombreClient
