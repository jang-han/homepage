from turtle import update
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Dish, Ingredient, Course, Type
from django.core.paginator import Paginator
from .forms import FindForm
from django.utils import timezone

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

def ingredient(request, num=1):
    msg = '食材名を入力してください。'
    ingredient_count = Ingredient.objects.all().count()
    ingredient_list = Ingredient.objects.all().order_by('id').reverse()
    page = Paginator(ingredient_list, 10)
    
    params = {
        'page' : 'top/ingredient.html',
        'msg' : msg,
        'ingredient_count' : ingredient_count,
        'ingredient_list' : page.get_page(num),   
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

def search(request, num=1):
    msg = '食材名を入力してください。'
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        result = Ingredient.objects.filter(ingredient__icontains=find) 
        msg = "が含まれた食材が「" + str(result.count()) + "」件検索されました。"
        if (result.count() == 0):
            msg = '0件が検索されました。'  
    else:
        form = FindForm()
    
    ingredient_list = Ingredient.objects.all().order_by('id').reverse()
    ingredient_count = Ingredient.objects.all().count()
    page = Paginator(ingredient_list, 10)
    
    params = {
        'page' : 'top/ingredient.html',
        'form' : form,
        'msg' : msg,
        'result' : result,
        'find' : find,
        'ingredient_list' : page.get_page(num),
        'ingredient_count' : ingredient_count,
    }
    return render(request, 'top/base.html', params)

def regist(request):
    params = {
        'page' : 'top/ingredient.html',
        'result_msg' : '',
    }
    if (request.method == 'POST') :
        new_ingredient = request.POST['new_ingredient']
        ingredient = Ingredient(ingredient=new_ingredient, regist=timezone.datetime.now(), update=timezone.datetime.now())
        ingredient.save()
        return redirect(to='/top/ingredient')
    
    return render(request, 'top/base.html', params)