from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    door_number = models.IntegerField(default=5)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.brand

class Motorcycle(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.brand