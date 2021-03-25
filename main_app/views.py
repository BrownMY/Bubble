from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Waters
from django.http import HttpResponse

class WaterCreate(CreateView):
    model = Waters
    fields = '__all__'
    success_url = '/water'

class WaterUpdate(UpdateView):
    model = Waters
    fields = ['brand', 'sizeoz', 'watertype']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/water/' + str(self.object.pk))

class WaterDelete(DeleteView):
    model = Waters
    success_url = '/water'

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

    