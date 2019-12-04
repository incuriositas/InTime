# InTime

------

- 제주대학교 SW융합캡스톤디자인II 수업 및 SW캡스톤디자인 발표 프로젝트
- 주제 : [제주 -> 김포] / [김포 -> 제주] 항공편 지연율 예측

- 사용한 예측 모델 : 랜덤포레스트 (Random Forest)
- 실시간 공항 날씨 : [AerisWeather](https://www.aerisweather.com/support/docs/api/)
- 실시간 항공편 현황 API : [공공데이터포털 - 항공기 운항정보](https://www.data.go.kr/subMain.jsp#/L3B1YnIvcG90L215cC9Jcm9zTXlQYWdlL29wZW5EZXZEZXRhaWxQYWdlJEBeMDgyTTAwMDAxMzBeTTAwMDAxMzUkQF5wdWJsaWNEYXRhRGV0YWlsUGs9dWRkaToxODVmMzBhYi0yZmZkLTQ5YTYtYmQ3Mi04ZWU4MzgzYzI5NTAkQF5wcmN1c2VSZXFzdFNlcU5vPTg4OTIxMjckQF5yZXFzdFN0ZXBDb2RlPVNUQ0QwMQ==)

------

- 웹 구동하기

  > 웹을 구동하기 위해서는 AerisWeather와 항공기 운항정보의 API 의 서비스키가 필요합니다.
  >
  > 1. predict.py 의 client_id 와 client_secret에는 AerisWeather 회원가입 후 Account - Demo Project의 ID와 SECRET을 넣으면 됩니다.
  > 2. getState.py의 key에는 공공데이터포털 회원 가입 후 항공기 운항정보 API 활용 신청 후 발급받은 서비스키를 넣으면 됩니다.

  > 서비스키를 입력 후 콘솔 명령을 입력하면 서버가 구동 됩니다.
  >
  > <pre>
  >   python3 manage.py runserver
  > </pre>
  >
  > 서버 구동 후 http://127.0.0.1:8000 로 접속하시면 웹 안에서 항공편 지연율을 예측 할 수 있습니다.
  >
  > 

------

- 웹에서 항공편 지연율 예측하기

![githubImage](https://github.com/incuriositas/InTime/blob/master/intimeScreenShot.png)

    > 1. airline : 항공사 선택
    > 2. airport : 출발 공항 선택
    > 3. arrived : 도착 공항 선택
    > 4. date : 항공편의 출발 시간 선택 (날짜와 시간대만 반영됨, 분 반영 X)

> Today's Real-Time Flight는 사용자가 최종적으로 선택한 시간대의 정각부터 10개 항공편의 실시간 현황을 보여줍니다.

