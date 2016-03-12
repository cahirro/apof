from django.db import models

# Create your models here.
class HungryPeople (models.Model):
    imie = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=128)

class Restaurants (models.Model):
    nazwa = models.CharField(max_length=128)
    otwarte_od = models.SmallIntegerField(max_length=5)
    otwarte_do = models.SmallIntegerField(max_length=5)
    adres = models.CharField(max_length=128)
    telefon = models.CharField(max_length=9)