from django.contrib import admin
from .models import Dish, Type, Course, Ingredient

# Register your models here.
admin.site.register(Dish)
admin.site.register(Type)
admin.site.register(Course)
admin.site.register(Ingredient)