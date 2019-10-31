import pandas as pd
import pickle
from sklearn.externals import joblib

from_pk = joblib.load('intime.pkl')

import urllib
import json
from datetime import datetime

now = datetime.now()


def getWeather(origin, day, time):
    if origin == 'jeju':
        originName = 'jeju,kr'
    elif origin == 'gmp':
        originName = 'seoul,kr'
    else:
        print("출발지를 입력 오류")

    wind_dir = 0
    temp = 22.5
    num = 0

    if day == now.day:
        num = time - (now.hour)
    else:
        num = time + (24 - now.hour)

    request = json.loads(urllib.request.urlopen(
        'https://api.aerisapi.com/forecasts/' + originName + '?&format=json&filter=1hr&limit=120&client_id=JubiGF1T5mtONfrcjWZpr&client_secret=GQ8ApghMTIAlQaX5KwRvXY7EDhZUy8UrzvtRHi6m')
                         .read())
    res = request['response']
    periods = res[0]['periods']

    if request['success']:
        periods[0]['dateTimeISO']
        TMP = periods[num]['avgTempC'] * 10
        CA_TOT = periods[num]['sky']
        TD = periods[num]['dewpointC'] * 10
        WSPD = periods[num]['windSpeedKTS']
        wind_dir = periods[num]['windDirDEG']
        for i in range(2, 16):
            if wind_dir < 22.5:
                wind_dir = 0
            elif temp * (i - 1) <= wind_dir and wind_dir < (temp * i):
                wind_dir = i
                break
        WD = wind_dir
        PA = periods[num]['pressureMB'] * 10
    else:
        print("An error occurred: %s" % (json['error']['description']))
        request.close()
    return [TMP, CA_TOT, TD, WSPD, WD, PA]

weather = getWeather('jeju',31,19)

def predict_delay(departure_date_time, weekend, airport, origin, destination, weather):
    from datetime import datetime

    try:
        departure_date_time_parsed = datetime.strptime(departure_date_time, '%d/%m/%Y %H:%M:%S')
    except ValueError as e:
        return 'Error parsing date/time - {}'.format(e)

    year = departure_date_time_parsed.year
    month = departure_date_time_parsed.month
    day = departure_date_time_parsed.day
    hour = departure_date_time_parsed.hour

    origin = origin.upper()
    destination = destination.upper()

    input = [{'CA_TOT': weather[1],
              'Date': year*10000+month*100+day,
              'PA' : weather[5],
              'TD': weather[2],
              'TMP' : weather[0],
              'Time': hour,
              'WD' : weather[4],
              'WSPD': weather[3],
              '항공사_대한항공': 1 if origin == '대한항공' else 0,
              '항공사_아시아나항공': 1 if origin == '아시아나항공' else 0,
              '항공사_에어부산': 1 if origin == "에어부산" else 0,
              '항공사_에어필립': 1 if origin == '에어필립' else 0,
              '항공사_이스타항공': 1 if origin == '이스타항공' else 0,
              '항공사_제주항공': 1 if origin == '제주항공' else 0,
              '항공사_진에어': 1 if origin == '진에어' else 0,
              '항공사_티웨이항공': 1 if origin == '티웨이항공' else 0,
              'ORIGIN_김포공항': 1 if origin == '김포' else 0,
              'ORIGIN_제주공항': 1 if origin == '제주' else 0,
              'DEST_김포공항': 1 if destination == '김포' else 0,
              'DEST_제주공항': 1 if origin == '제주' else 0,
              'weekend_FRI': 1 if destination == '금' else 0,
              'weekend_MON': 1 if destination == '월' else 0,
              'weekend_SAT': 1 if destination == '토' else 0,
              'weekend_SUN': 1 if destination == '일' else 0,
              'weekend_THU': 1 if destination == '목' else 0,
              'weekend_TUE': 1 if destination == '화' else 0,
              'weekend_WED': 1 if destination == '수' else 0,
            }]
    return from_pk.predict(pd.DataFrame(input))[0]

predict_delay('31/10/2019 19:00:00','목', '제주','제주', '김포', weather)