from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponsefrom django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
import urllib.request
import json
import os


def lyft_json(lon1, lat1,lon2,lat2):
	'''data = urllib.parse.urlencode({
		"grant_type": "client_credentials", "scope" : "public"
		})
	data = data.encode('ascii')
	request_access = urllib.request.Request('https://api.lyft.com/oauth/token', data=data )
	request_access.add_header('Content-Type', 'application/json')
	#request_access.add_header('Authorization', '%s:%s'%("BOWOhdm8oYl9", os.environ.get('LYFT_SECRET')))
	request_access.add_header('Content-Length', str(request_access.data.__sizeof__()))
	print('requesting access')
	access_response = urllib.request.urlopen(request_access)
	print('received access')
	access = json.load(access_response)
	cmd = """curl -X POST -H "Content-Type: application/json" \
     --user "%s:%s" \
     -d '{"grant_type": "authorization_code", "code": "<authorization_code>"}' \
     'https://api.lyft.com/oauth/token'"""%("BOWOhdm8oYl9", os.environ.get('LYFT_SECRET'))
'''

	request = urllib.request.Request('https://api.lyft.com/v1/cost?start_lat=%f&start_lng=%f&end_lat=%f&end_lng=%f' %(lon1,lat1,lon2,lat2))
	request.add_header('Authorization', 'Bearer %s' %os.getenv('LYFT_KEY'))
	response = urllib.request.urlopen(request)
	data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
	print(data)

	for i in data.get('cost_estimates'):
		if i.get("ride_type") == 'lyft':
			data = i.copy()
	return data
