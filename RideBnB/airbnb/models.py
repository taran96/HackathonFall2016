from django.db import models

# Create your models here.

class Room(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    p_type = models.CharField(max_length=1, choices=(("T", "Townhouse"), ("C", "Condominium"),( "A", "Apartment"), ("H", "House")))
    price = models.FloatField()
    desc = models.TextField()
    air_id = models.IntegerField()
    title = models.TextField()
    location = models.TextField()
    pic_url = models.TextField()
