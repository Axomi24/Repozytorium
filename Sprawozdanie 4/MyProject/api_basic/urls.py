from django.urls import path
from .views import CarAPIView, GenericAPIView

urlpatterns = [
    path('car/', CarAPIView.as_view()),
    path('generic/car/<int:id>/', GenericAPIView.as_view()),
]