from dataclasses import field
from rest_framework import serializers
from .models import (
    CarMake,
    CarModel,
    Trim,
    Car
)


class CarMakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarMake
        fields = ['id', 'name']


class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = ['id', 'car_make', 'name']


class TrimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trim
        fields = ['id', 'car_make', 'car_model', 'name']


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id',
                  'car_make',
                  'car_model',
                  'car_trim',
                  'engine_cc',
                  'body',
                  'gear',
                  'drive_type',
                  'version',
                  'mpg',
                  'market_price',
                  'similar',
                  'description']
