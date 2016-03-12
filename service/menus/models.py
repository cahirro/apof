from django.db import models

# Create your models here.

class Restaurants (models.Model):
    nazwa = models.CharField(max_length=128)
    otwarte_od = models.CharField(max_length=5)
    otwarte_do = models.CharField(max_length=5)
    adres = models.CharField(max_length=128)
    telefon = models.CharField(max_length=9)