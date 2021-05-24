from rest_framework import serializers
from .models import Car, Motorcycle

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=['id','brand','name','door_number','color']

class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Motorcycle
        fields=['id','brand','name','color']
