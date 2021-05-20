from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Car
from .serializers import CarSerializer
# Create your views here.

def article_list(request):
    if request.method=='GET':
        cars=Car.objects.all()
        serializers= CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.methon == 'POST':
        data = JSONParser().parse(request)
        serializer=CarSeliarizer(data=data)
