from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponse

from airbnb.models import Room
from ride.views import lyft_json


def give_airbnb(request):
    longi = float(request.GET.get("lon"))
    lati = float(request.GET.get("lat"))
    data = serializers.serialize(
        "json",
        Room.objects.filter(
            lon__range=(longi - 0.009, longi + 0.009),
            lat__range=(lati - 0.009, lati + 0.009)))
    return HttpResponse(data, content_type="application/json")


def give_dest_info(request):
    lon = float(request.POST.get("lon"))
    lat = float(request.POST.get("lat"))
    if not (lon and lat):
        lon = float(request.GET.get("lon"))
        lat = float(request.GET.get("lat"))
