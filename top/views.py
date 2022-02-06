from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'monthly':'Monthly Meal Plan',
    }
    return render(request, 'top/index.html', params)

def monthly(request):
    params = {
        
    }
    return render(request, 'top/monthly.html', params)
# Create your views here.
