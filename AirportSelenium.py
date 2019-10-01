# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://www.airportal.go.kr/life/airinfo/RbHanFrm.jsp")
def setDate(datevalue):
    date = driver.find_element_by_xpath('//*[@id="current_date"]')
    date.click()
    date.clear()
    date.click()
    date.send_keys(str(datevalue))
def setAirport(airportvalue):
    airport = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/span/select/option['+str(airportvalue)+']').click()
def setDivision(d):
    if d==0:
        path = '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input[1]'
    else:
        path = '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input[2]'
        
    driver.find_element_by_xpath(path).click()
def Search():
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/a/img").click()
def Data(d,airportvalue,date):
    #d=0이면 도착
    setDivision(d)
    #airportvalue==2 : 김포 or airportvalue==8 : 제주 
    setAirport(airportvalue)
    setDate(date)
    Search()
Data(1,8,20190901)
l = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[5]/td/iframe')
driver.switch_to_frame(l)
li = [i.split() for i in driver.find_element_by_tag_name("table").text.split('\n')]
print(li)