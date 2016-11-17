import os
import sys
import glob
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RideBnB.settings")
django.setup()

from airbnb.models import Room

csvFiles = glob.glob("csvs/*.csv")

def get_amenities(lst):
    nested_list = []

    for i in lst:
        new_list = []
        new_list.append("TV" in i)
        new_list.append('Internet' in i)
        new_list.append("Air Conditioning" in i)
        new_list.append("Kitchen" in i)
        new_list.append("Heating" in i)
        nested_list.append(new_list)
    return nested_list

for i in csvFiles:
    columns = {}
    reader = csv.reader(open(i, "r"))
    headers = next(reader, None)
    for j in headers:
        columns[j] = []
    for row in reader:

        for h, v in zip(headers,row):

            columns[h].append(v)

    needed_data = {}
    needed_data['lon'] = list(map(float, columns["longitude"]))
    needed_data['lat'] = list(map(float, columns["latitude"]))
    needed_data['p_type'] = columns["property_type"]
    needed_data['air_id'] = list(map(int, columns["id"]))
    needed_data['price'] = list(map(lambda x: float(x[1:].replace(",","")),columns["price"]))
    needed_data['desc'] = columns["summary"]
    needed_data['title'] = columns["name"]
    needed_data['pic_url'] = columns["picture_url"]



    amenities = get_amenities(list(columns['amenities']))
    needed_data["tv"] = []
    needed_data["wifi"] = []
    needed_data["ac"] = []
    needed_data["kitchen"] = []
    needed_data["heating"] = []
    for i in amenities:
        needed_data["tv"].append(i[0])
        needed_data["wifi"].append(i[1])
        needed_data["ac"].append(i[2])
        needed_data["kitchen"].append(i[3])
        needed_data["heating"].append(i[4])

    new_needs = needed_data.copy()
    for i in range(len(needed_data['lon'])):
        kwargs = {}
        for key, val in new_needs.items():
            kwargs[key] = new_needs[key][i]

        r = Room(**kwargs)
        r.save()
