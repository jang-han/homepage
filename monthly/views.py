from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        
    }
    return render(request, 'monthly/index.html', params)