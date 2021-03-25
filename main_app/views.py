from django.shortcuts import render
from .models import Waters
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h3>Detroit says: What up Doe? Drink some water.</h3>')

def bubble(request):
    return HttpResponse('Hydration meter:')

def about(request):
    return render(request, 'about.html')

def water_index(request):
    water = Waters.objects.all()
    return render(request, 'water/index.html', {'water': water})

def water_show(request, water_id):
    water = Waters.objects.get(id=water_id)
    return render(request, 'water/show.html', {'water': water})

    