from django.shortcuts import render
from django.core import serializers
from airbnb.models import Room
from django.http import JsonResponse

# Create your views here.

def give_airbnb(request):
    lon = float(request.POST.get("lon"))
    lat = float(request.POST.get("lat"))
    if not (lon and lat):
        lon = float(request.GET.get("lon"))
        lat = float(request.GET.get("lat"))
    upleft = (lon - 0.01, lat + 0.01)
    downright = (lon + 0.01, lat - 0.01)
    data = serializers.serialize("json", Room.objects.filter(lon__range=(upleft[0], downright[0]), lat__range=(downright[1], upleft[1])))
    return JsonResponse(data, safe=False)
