import requests
from bs4 import BeautifulSoup
from urllib import parse

key = "key"
url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?'

num = 1
query = {
    'serviceKey': key,
    'schAirCode': 'GMP',
    'pageNo': num,
}

# xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
# response = requests.get(xmlUrl)
# soup = BeautifulSoup(response.text, 'lxml')

for i in range(4):
    xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
    response = requests.get(xmlUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    num += 1

print(response.text)
print(soup.find_all('city'))
