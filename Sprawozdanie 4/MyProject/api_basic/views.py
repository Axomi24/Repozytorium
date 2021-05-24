from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Car
from .serializers import CarSerializer
from .models import Motorcycle
from .serializers import MotorcycleSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request, id=None):
        return self.update(request,id)

    def delete(self,request, id):
        return self.destroy(request,id)

class CarAPIView(APIView):
    def get(self, request):
        cars=Car.objects.all()
        serializer= CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=CarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MotorcycleGenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=MotorcycleSerializer
    queryset=Motorcycle.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request, id=None):
        return self.update(request,id)

    def delete(self,request, id):
        return self.destroy(request,id)

class MotorcycleAPIView(APIView):
    def get(self, request):
        Motorcycles=Motorcycle.objects.all()
        serializer= MotorcycleSerializer(Motorcycles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=MotorcycleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
