from EBApi.serializers import PropertySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import requests

class PropertyList(APIView):
    """List a page of properties."""

    headers = {
        'X-Authorization': 'l7u502p8v46ba3ppgvj5y2aad50lb9'
    }

    base_url = 'https://api.stagingeb.com/v1/properties?page=1&limit=15'

    def __init__(self):
        self.response = self.make_request(self.base_url)
    
    def make_request(self, base_url):
        """Genera el response inicial."""

        response = requests.get(base_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()

    def get(self, request):
        data = self.response['content']
        results = PropertySerializer(data, many=True).data
        return Response(results)