from django.db import models

# Create your models here.

class Passengers(models.Model):
    
    First_Name = models.CharField(max_length= 20)
    Last_Name = models.CharField(max_length=20)
    Birth = models.DateField()
    Passport_Number = models.CharField(max_length=8, unique=True)

class Flights(models.Model):
    
    Flight_Number = models.CharField(max_length = 8)
    Departure = models.CharField(max_length=50)
    Destination = models.CharField(max_length=50, null=True)
    Departure_date = models.DateField()
    Return_date = models.DateField(blank=True)
    CarryOn = models.IntegerField(blank=True)
    Trolley = models.IntegerField(blank=True)
    CheckIn = models.IntegerField(blank=True)
    PassangerId = models.ForeignKey(Passengers, on_delete=models.CASCADE)