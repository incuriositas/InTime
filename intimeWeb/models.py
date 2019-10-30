from django.conf import settings
from django.db import models
from django.utils import timezone


class Flight(models.Model):
    # 사용자의 입력
    airline = models.CharField(max_length=20)  # 항공사
    airport = models.CharField(max_length=50)  # 출발 공항
    arrived = models.CharField(max_length=50)  # 도착 공항
    date = models.IntegerField(default=0)  # 날짜
    time = models.IntegerField(default=0)  # 시간
    day = models.CharField(max_length=10, null=True)  # 요일

    # 예측하여 저장할 결과
    delayRate = models.IntegerField(default=0, null=True, blank=True)  # 지연률
    state = models.CharField(max_length=10, null=True, blank=True)     # 상태(현황)

    def __str__(self):
        return "%s / %s / %s " %(self.airline, self.airport, self.delayRate)
