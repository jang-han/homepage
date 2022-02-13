from django.http import HttpResponse
from django.shortcuts import render
from .models import Dish, Ingredient, Course, Type

# Create your views here.
def index(request):
    params = {
        '' : '',
    }
    return render(request, 'top/index.html', params)

def top(request):
    # data = Dish.objects.all().values('ingredient1','ingredient2','ingredient3','ingredient4','ingredient5','course','type')
    total_count = Dish.objects.all().count()
    western_food = Dish.objects.filter(course=1)
    japanese_food = Dish.objects.filter(course=2)
    korean_food = Dish.objects.filter(course=3)
    breakfast = Dish.objects.filter(type=1)
    lunch = Dish.objects.filter(type=2)
    dinner = Dish.objects.filter(type=3)
    western_food_count = western_food.count()
    japanese_food_count = japanese_food.count()
    korean_food_count = korean_food.count()
    breakfast_count = breakfast.count()
    lunch_count = lunch.count()
    dinner_count = dinner.count()
    
    
    params = {
        'page' : 'top/top.html',
        'total_count' : total_count,
        'western_food_count' : western_food_count,
        'japanese_food_count' : japanese_food_count,
        'korean_food_count' : korean_food_count,
        'breakfast_count' : breakfast_count,
        'lunch_count' : lunch_count,
        'dinner_count' : dinner_count,
        # 'data' : data,
    }
    return render(request, 'top/base.html', params)

def refrigerator(request):
    params = {
        'page' : 'top/refrigerator.html',
    }
    return render(request, 'top/base.html', params)

def dishes(request):
    params = {
        'page' : 'top/dishes.html',
    }
    return render(request, 'top/base.html', params)

def dishschedule(request):
    params = {
        'page' : 'top/dishschedule.html',
    }
    return render(request, 'top/base.html', params)

def components(request):
    params = {
        'page' : 'top/components.html',
    }
    return render(request, 'top/base.html', params)

def project(request):
    params = {
        'page' : 'top/project.html',
    }
    return render(request, 'top/base.html', params)