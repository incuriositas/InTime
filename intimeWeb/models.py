from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from .widgets import XDSoftDateTimePickerInput


class Flight(models.Model):
    # 사용자의 입력
    airline_choice = (
        ('대한항공', '대한항공'),
        ('아시아나항공', '아시아나항공'),
        ('에어부산', '에어부산'),
        ('에어필립', '에어필립'),
        ('티웨이항공', '티웨이항공'),
        ('제주항공', '제주항공'),
        ('이스타항공', '이스타항공'),
        ('진에어', '진에어')
    )
    airport_choice = (
        ('제주공항', '제주공항'),
        ('김포공항', '김포공항')
    )

    airline = models.CharField(max_length=20, choices=airline_choice)  # 항공사
    airport = models.CharField(max_length=50, choices=airport_choice)  # 출발 공항
    arrived = models.CharField(max_length=50, choices=airport_choice)  # 도착 공항
    date = models.DateTimeField()  # 날짜

    # 예측하여 저장할 결과
    delayRate = models.IntegerField(default=0, null=True, blank=True)  # 지연률
    state = models.CharField(max_length=10, null=True, blank=True)     # 상태(현황)

    def __str__(self):
        return "%s에서 %s시에 출발하는 %s의 지연률은 %s입니다." %(self.airport, str(self.date)[:13], self.airline, self.delayRate)
