from django.conf import settings
from django.db import models
from django.utils import timezone


class Flight(models.Model):
    airFln = models.CharField(max_length=20, primary_key=True)
    airline = models.CharField(max_length=20)
    airport = models.CharField(max_length=50)
    arrived = models.CharField(max_length=50)
    boarding = models.CharField(max_length=50)
    schTime = models.DateTimeField(default=timezone.now())
    predictTime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.airFln, self.predictTime)