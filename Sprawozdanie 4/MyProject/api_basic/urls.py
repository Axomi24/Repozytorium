from django.urls import path
from .views import car_list, car_detail, CarAPIView, CarDetails, GenericAPIView

urlpatterns = [
    #path('car/', car_list),
    path('car/', CarAPIView.as_view()),
    #path('detail/<int:pk>/', car_detail),
    path('detail/<int:id>/', CarDetails.as_view()),
    path('generic/car/<int:id>/', GenericAPIView.as_view()),
]