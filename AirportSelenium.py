# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("http://www.airportal.go.kr/life/airinfo/RbHanFrm.jsp")

#날짜 선택
def setDate(datevalue):
    date = driver.find_element_by_xpath('//*[@id="current_date"]')
    date.click()
    date.clear()
    date.click()
    date.send_keys(str(datevalue))

#공항 선택 : 김포(2) 제주(8)
def setAirport(airportvalue):
    airport = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/span/select/option['+str(airportvalue)+']').click()

#구분 선택 : 도착(0),출발(1) 클릭
def setDivision(d):
    if d==0:
        path = '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input[1]'
    else:
        path = '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input[2]'
        
    driver.find_element_by_xpath(path).click()

#검색버튼 클릭
def Search():
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/a/img").click()

#한번에 데이터 검색
def Data(d,airportvalue,date):
    #d=0이면 도착
    setDivision(d)
    #airportvalue==2 : 김포 or airportvalue==8 : 제주 
    setAirport(airportvalue)
    setDate(date)
    Search()

#검색한 데이터 가져오기
FlightData = list()
def Run(Date):
    Data(1,8,Date)
    result = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[5]/td/iframe')
    driver.switch_to_frame(result)
    FlightData.append([[Date]+i.split() for i in driver.find_element_by_tag_name("table").text.split('\n')])
    driver.switch_to_default_content()

#18년도 10월 - 19년도 9월
end_date = [31,30,31,31,28,31,30,31,30,31,31,30]

#20181001 - 20191001까지 데이터 검색
Date = 20181000
i = 0

while(Date<20190931): 
    day = Date%100
    month = ((Date%10000)-day)/100
    year = (Date-(Date%10000))/10000
    day = day + 1
    if day > end_date[i]:
        day = 1
        month = month + 1
        i = i+1
        if month == 13:
            year = year + 1
            month = 1
            day = 1
    Date = int((year*10000)+(month*100)+day)
    Run(Date)

#csv파일생성
data = pd.DataFrame(FlightData)
data.to_csv('제주출발.csv', encoding='cp949')