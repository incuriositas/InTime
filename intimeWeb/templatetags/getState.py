import requests
from bs4 import BeautifulSoup
from urllib import parse

# -*- coding: UTF-8 -*-
import logging
from django import template

register = template.Library()

@register.simple_tag
def test_tag():
    xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
    response = requests.get(xmlUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


key = "key"
url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?'

num = 1
query = {
    'serviceKey': key,
    'schAirCode': 'GMP',
    'pageNo': num,
}

test = test_tag()
# xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
# response = requests.get(xmlUrl)
# soup = BeautifulSoup(response.text, 'lxml')
#
# for i in range(4):
#     xmlUrl = url + parse.urlencode(query, encoding='UTF-8', doseq=True, safe="%")
#     response = requests.get(xmlUrl)
#     soup = BeautifulSoup(response.text, 'lxml')
#     num += 1
#
# print(response.text)
# print(soup.find_all('city'))
