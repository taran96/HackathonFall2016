from django.db import models
from django.contrib.auth.models import User


class Destinations(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User)
