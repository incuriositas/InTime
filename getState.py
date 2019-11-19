import requests
from urllib import parse
import xml.etree.ElementTree as elemtree
import datetime


key = "key"
url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?'


# xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
# response = requests.get(xmlUrl)
# soup = BeautifulSoup(response.text, 'lxml')

# for i in range(4):
#     xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
#     response = requests.get(xmlUrl)
#     soup = BeautifulSoup(response.text, 'lxml')
#     num += 1

# print(response.text)
def cal_time(hour):
    if hour <= 6:
        time = '0600'
    elif 6 < hour < 10:
        time = '0' + str(hour) + '00'
    else:
        time = str(hour) + '00'
    return time


def get_state(airport):
    state_list = []
    num = 0
    if airport == 'CJU':
        for a in range(25):
            query = {
                'serviceKey': key,
                'schAirCode': 'CJU',
                'schIOType': 'O',
                'schLineType': 'D',
                'schStTime': cal_time(datetime.datetime.now().hour),
                'schEdTime': '2200',
                'pageNo': a,
            }
            xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
            response = requests.get(xmlUrl)
            tree = elemtree.fromstring(response.text)
            for i in tree.findall('body'):
                for j in i.findall('items'):
                    for k in j.findall('item'):
                        temp = []
                        if k.find('arrivedKor').text == '서울/김포' and num < 10:
                            num += 1
                            temp.append(k.find('airlineKorean').text)
                            temp.append(k.find('airFln').text)
                            temp.append(k.find('boardingKor').text)
                            temp.append(k.find('arrivedKor').text)
                            temp.append(k.find('std').text[0:2] + ':' + k.find('std').text[2:4])
                            if k.find('etd') is not None:
                                temp.append(k.find('etd').text[0:2] + ':' + k.find('etd').text[2:4])
                        else:
                            pass
                        state_list.append(temp)
    elif airport == 'GMP':
        for a in range(25):
            query = {
                'serviceKey': key,
                'schAirCode': 'GMP',
                'schIOType': 'O',
                'schLineType': 'D',
                'schStTime': cal_time(datetime.datetime.now().hour),
                'schEdTime': '2200',
                'pageNo': a,
            }
            xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
            response = requests.get(xmlUrl)
            tree = elemtree.fromstring(response.text)
            for i in tree.findall('body'):
                for j in i.findall('items'):
                    for k in j.findall('item'):
                        temp = []
                        if k.find('arrivedKor').text == '제주' and num < 10:
                            num += 1
                            temp.append(k.find('airlineKorean').text)
                            temp.append(k.find('airFln').text)
                            temp.append(k.find('boardingKor').text)
                            temp.append(k.find('arrivedKor').text)
                            temp.append(k.find('std').text[0:2] + ':' + k.find('std').text[2:4])
                            if k.find('etd') is not None:
                                temp.append(k.find('etd').text[0:2] + ':' + k.find('etd').text[2:4])
                        else:
                            pass
                        state_list.append(temp)

    return state_list
