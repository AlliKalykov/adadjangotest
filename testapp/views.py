from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelName, SecondModel

def home(request):
    return HttpResponse("Hello, World!")

def index(request):
    return render(request, 'index.html')

def model_name_view(request):
    model_name = ModelName.objects.all()
    context = {
        "datas": model_name,
    }
    return render(request, 'home.html', context)
