from django.contrib import admin

# Register your models here.
from .models import (
    CarMake,
    CarModel,
    Trim,
    Car
)
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Trim)
admin.site.register(Car)
