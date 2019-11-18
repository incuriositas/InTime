from django.http import QueryDict

from .models import Flight
from django.shortcuts import render, redirect, HttpResponse
from .form import SearchForm
from predict import predict_delay, getWeather, get_day


def index(request):
    flights = Flight.objects.last()
    form = SearchForm(request.POST)
    return render(request, 'intimeWeb/index.html', {'flights': flights,
                                                    'form': form})


def form_func(request):
    flight = Flight.objects.last()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.data.dict()
            month = int(data['date'][0:2])
            day = int(data['date'][3:5])
            year = int(data['date'][6:10])
            hour = int(data['date'][11:13])
            weather = getWeather(data['airport'], day, hour)
            print(weather)
            data['delayRate'] = predict_delay(year, month, day, hour, get_day(month, day), data['airport'],
                                              data['airport'],  data['arrived'], weather)
            print(data['delayRate'])
            new_dict = QueryDict('', mutable=True)
            new_dict.update(data)
            new_form = SearchForm(new_dict)
            post = new_form.save(commit=False)  # 중복 DB save를 방지
            post.ip = request.META['REMOTE_ADDR']  # ip 필드는 유저로 부터 입력 받지 않고 프로그램으로 채워 넣는다
            post.save()
            return redirect('.')
    else:
        form = SearchForm()
    return render(request, 'intimeWeb/index.html', {'form': form, 'flight': flight})

