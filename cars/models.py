from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_car_makes(cls):
        car_makes = cls.objects.all()
        return car_makes

    @classmethod
    def get_single_car_make(cls, pk):
        car_make = get_object_or_404(cls, pk=pk)
        return car_make


class CarModel(models.Model):
    car_make = models.ForeignKey(to=CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_car_models(cls):
        car_models = cls.objects.all()
        return car_models

    @classmethod
    def get_single_car_model(cls, pk):
        car_model = get_object_or_404(cls, pk=pk)
        return car_model


class Trim(models.Model):
    car_make = models.ForeignKey(to=CarMake, on_delete=models.CASCADE)
    car_model = models.ForeignKey(to=CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_trims(cls):
        trims = cls.objects.all()
        return trims

    @classmethod
    def get_single_trim(cls, pk):
        trim = get_object_or_404(cls, pk=pk)
        return trim


class Car(models.Model):
    car_make = models.ForeignKey(to=CarMake, on_delete=models.DO_NOTHING)
    car_model = models.ForeignKey(to=CarModel, on_delete=models.DO_NOTHING)
    car_trim = models.ForeignKey(to=Trim, on_delete=models.DO_NOTHING)
    engine_cc = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    gear = models.CharField(max_length=255)
    drive_type = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    mpg = models.CharField(max_length=255)
    market_price = models.IntegerField()
    similar = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.car_make)

    @classmethod
    def get_cars(cls):
        cars = cls.objects.all()
        return cars

    @classmethod
    def get_single_car(cls, pk):
        car = get_object_or_404(cls, pk=pk)
        return car

    @classmethod
    def get_cars_of_make(cls, car_make):
        cars = get_object_or_404(cls, car_make=car_make)
        return cars

    @classmethod
    def get_cars_of_model(cls, car_model):
        cars = get_object_or_404(cls, car_model=car_model)
        return cars

    @classmethod
    def get_cars_of_trim(cls, car_trim):
        cars = get_object_or_404(cls, car_trim=car_trim)
        return cars
