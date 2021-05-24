from django.urls import path
from .views import CarAPIView, GenericAPIView, MotorcycleAPIView, MotorcycleGenericAPIView

urlpatterns = [
    path('car/', CarAPIView.as_view()),
    path('generic/car/<int:id>/', GenericAPIView.as_view()),
    path('motorcycle/', MotorcycleAPIView.as_view()),
    path('generic/motorcycle/<int:id>/', MotorcycleGenericAPIView.as_view()),
]