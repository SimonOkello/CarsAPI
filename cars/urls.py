from django.urls import path
from .views import (
    CarAPIView,
    CarDetailAPIView,
    CarMakeAPIView,
    CarMakeDetailAPIView,
    CarModelAPIView,
    CarModelDetailAPIView,
    CarTrimAPIView,
    CarTrimDetailAPIView

)

urlpatterns = [
    path('', CarAPIView.as_view(), name='cars-api'),
    path('car-detail/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail-api'),
    path('car-make/', CarMakeAPIView.as_view(), name='car-make-api'),
    path('car-make-detail/<int:pk>/', CarMakeDetailAPIView.as_view(),
         name='car-make-detail-api'),
    path('car-model/', CarModelAPIView.as_view(), name='car-model-api'),
    path('car-model-detail/<int:pk>/', CarModelDetailAPIView.as_view(),
         name='car-make-detail-api'),
    path('car-trim/', CarTrimAPIView.as_view(), name='car-trim-api'),
    path('car-trim-detail/<int:pk>/', CarTrimDetailAPIView.as_view(),
         name='car-trim-detail-api'),
]
