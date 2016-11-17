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
    p_type = models.CharField(
        max_length=1,
        choices=(("T", "Townhouse"), ("C", "Condominium"), ("A", "Apartment"),
                 ("H", "House")),
        null=True)
    price = models.FloatField(null=True)
    desc = models.TextField(null=True)
    air_id = models.IntegerField()
    title = models.TextField(null=True)
    location = models.TextField(null=True)
    pic_url = models.TextField(null=True)

    def __str__(self):
        return self.title
