from django.shortcuts import render
from .models import Flight
from django.shortcuts import render, redirect, HttpResponse
from .form import SearchForm
from predict import predict_delay, getWeather, get_day


def index(request):
    flights = Flight.objects.all()
    return render(request, 'intimeWeb/index.html', {'flights': flights})


def search(request, pk):
    flight = Flight.objects.get(pk=pk)
    return render(request, 'intimeWeb/search.html', {'flight': flight})


def form_func(request):
    flight = Flight.objects.last()
    weather = getWeather(flight.airport, int(str(flight.date)[8:10]), int(str(flight.date)[11:13]))
    flight.delayRate = predict_delay(int(str(flight.date)[0:4]), int(str(flight.date)[5:7]),
                                     int(str(flight.date)[8:10]), int(str(flight.date)[11:13]),
                                     get_day(int(str(flight.date)[8:10]), int(str(flight.date)[5:7])),
                                     flight.airport,
                                     flight.airport,
                                     flight.arrived,
                                     weather)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 중복 DB save를 방지
            post.ip = request.META['REMOTE_ADDR']  # ip 필드는 유저로 부터 입력 받지 않고 프로그램으로 채워 넣는다
            post.save()
            return redirect('.')
    else:
        form = SearchForm()
    return render(request, 'intimeWeb/form.html', {'form': form, 'flight': flight})

