from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .serializers import (
    CarMakeSerializer,
    CarModelSerializer,
    TrimSerializer,
    CarSerializer
)
from .models import (
    CarMake,
    CarModel,
    Trim,
    Car
)


class CarMakeAPIView(GenericAPIView):
    serializer_class = CarMakeSerializer
    queryset = CarMake.get_car_makes()

    def get(self, request):
        cars = self.get_queryset()
        serializer = self.serializer_class(cars, many=True)
        return Response({
            'responseCode': '0',
            'message': 'Car makes retrieved',
            'cars': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car make added',
            'cars': serializer.data
        }, status=status.HTTP_201_CREATED)


class CarMakeDetailAPIView(GenericAPIView):
    serializer_class = CarMakeSerializer
    queryset = CarMake.get_car_makes()

    def get(self, request, pk):
        car_make = Car.get_single_car_make(pk)
        serializer = self.serializer_class(car_make)
        return Response({
            'responseCode': '0',
            'message': 'Car make retrieved',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = request.data
        car_make = Car.get_single_car_make(pk)
        serializer = self.serializer_class(car_make, data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car make edited',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car_make = Car.get_single_car_make(pk)
        car_make.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarModelAPIView(GenericAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.get_car_models()

    def get(self, request):
        car_models = self.get_queryset()
        serializer = self.serializer_class(car_models, many=True)
        return Response({
            'responseCode': '0',
            'message': 'Car models retrieved',
            'cars': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car model added',
            'cars': serializer.data
        }, status=status.HTTP_201_CREATED)


class CarModelDetailAPIView(GenericAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.get_car_models()

    def get(self, request, pk):
        car_model = CarModel.get_single_car_model(pk)
        serializer = self.serializer_class(car_model)
        return Response({
            'responseCode': '0',
            'message': 'Car make retrieved',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = request.data
        car_model = CarModel.get_single_car_model(pk)
        serializer = self.serializer_class(car_model, data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car model edited',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car_model = CarModel.get_single_car_model(pk)
        car_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarTrimAPIView(GenericAPIView):
    serializer_class = TrimSerializer
    queryset = Trim.get_trims()

    def get(self, request):
        trims = self.get_queryset()
        serializer = self.serializer_class(trims, many=True)
        return Response({
            'responseCode': '0',
            'message': 'Car trims retrieved',
            'cars': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car trim added',
            'cars': serializer.data
        }, status=status.HTTP_201_CREATED)


class CarTrimDetailAPIView(GenericAPIView):
    serializer_class = TrimSerializer
    queryset = Trim.get_trims()

    def get(self, request, pk):
        car_trim = Trim.get_single_trim(pk)
        serializer = self.serializer_class(car_trim)
        return Response({
            'responseCode': '0',
            'message': 'Car trim retrieved',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = request.data
        car_trim = Trim.get_single_trim(pk)
        serializer = self.serializer_class(car_trim, data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car trim edited',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car_trim = Trim.get_single_trim(pk)
        car_trim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarAPIView(GenericAPIView):
    serializer_class = CarSerializer
    queryset = Car.get_cars()

    def get(self, request):
        cars = self.get_queryset()
        serializer = self.serializer_class(cars, many=True)
        return Response({
            'responseCode': '0',
            'message': 'Cars retrieved',
            'cars': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car added',
            'cars': serializer.data
        }, status=status.HTTP_201_CREATED)


class CarDetailAPIView(GenericAPIView):
    serializer_class = CarSerializer
    queryset = Car.get_cars()

    def get(self, request, pk):
        car = Car.get_single_car(pk)
        serializer = self.serializer_class(car)
        return Response({
            'responseCode': '0',
            'message': 'Car retrieved',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = request.data
        car = Car.get_single_car(pk)
        serializer = self.serializer_class(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'responseCode': '0',
            'message': 'Car edited!',
            'car': serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car = Car.get_single_car(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
