import json
import os
import urllib


def lyft_json(lon1, lat1, lon2, lat2):

    request = urllib.request.Request(
        'https://api.lyft.com/v1/cost?start_lat=%f&start_lng=%f&end_lat=%f&end_lng=%f'
        % (lon1, lat1, lon2, lat2))
    request.add_header('Authorization', 'Bearer %s' % os.getenv('LYFT_KEY'))
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode(response.info().get_param(
        'charset') or 'utf-8'))
    print(data)

    for i in data.get('cost_estimates'):
        if i.get("ride_type") == 'lyft':
            data = i.copy()
    return data
