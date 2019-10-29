from django.shortcuts import render
from .models import Flight
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    flights = Flight.objects.all()
    return render(request, 'intimeWeb/index.html', {'flights':flights})


def search(request, pk):
    flight = Flight.objects.get(pk=pk)
    return render(request, 'intimeWeb/search.html', {'flights':flight})

