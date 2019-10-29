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


key = "W%2FXqZYCB9W4EmWYdttyzqxMOyxiohhUEiB7zIzRzR0c%2BNF3rNi4ZOV8Zs%2Bb0PqrXpWhiwKNcWX%2FISD%2Bgt5oQnQ%3D%3D"
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
