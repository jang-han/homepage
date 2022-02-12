from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        '' : '',
    }
    return render(request, 'top/index.html', params)

def top(request):
    params = {
        'page' : 'top/top.html',
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