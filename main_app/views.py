from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h3>Detroit says: What up Doe? Drink some water.</h3>')

def bubble(request):
    return HttpResponse('Hydration meter:')

def about(request):
    return render(request, 'about.html')

