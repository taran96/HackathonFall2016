import json
from django.test import TestCase, Client, override_settings
from django.core.urlresolvers import reverse
from airbnb.views import give_airbnb


@override_settings(CACHE_MIDDLEWARE_SECONDS = 0)
class TestAPI(TestCase):

    fixtures = ['airbnb.json']

    def test_response_with_get(self):
        ''' Check for GET request's response '''
        response = self.client.get(
            "%s?lat=40.731&lon=-73.99" % reverse("airbnb_api_request")
        )
        self.assertEqual(response.status_code, 200)

    def test_response_with_post(self):
        ''' Check for POST request's response '''
        response = self.client.post(
            reverse("airbnb_api_request"),{ 'lat':40.714, "lon":-73.965})
        self.assertEqual(response.status_code, 200)

    def test_response_json_data(self):
        ''' Check if data in response is json compatible '''
        response = self.client.post(
            reverse("airbnb_api_request"),{ 'lat':40.731, "lon":-73.99})
        self.assertTrue(json.loads(str(response.content, 'utf-8')))

    def test_non_empty_response_content(self):
        ''' Check for non empty data from response '''
        response = self.client.post(
            reverse("airbnb_api_request"),{ 'lat':40.731, "lon":-73.99})
        self.assertNotEqual(response.content, b'[]')
        response = self.client.get(
            "%s?lat=40.731&lon=-73.99" % reverse("airbnb_api_request")
        )
        self.assertNotEqual(response.content, b'[]')
