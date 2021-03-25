from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h3>Detroit says: What up Doe? Drink some water.</h3>')

def bubble(request):
    return HttpResponse('Hydration meter:')

def about(request):
    return render(request, 'about.html')

def water_index(request):
    return render(request, 'water/index.html', {'water': water})

class Waters:
    def __init__(self, brand, sizeoz, watertype):
        self.brand = brand
        self.sizeoz = sizeoz
        self.watertype = watertype

water =  [
    Waters('Essentia', 20, 'Alkaline'),
    Waters('Absopure', 32, 'Spring'),
    Waters('Tap', 8, 'Tap')
]


    