from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from nasa.models import (
    NasaEvent
)
from datetime import datetime
import requests
from django.db import transaction

querystring = {
    "fragment":"true",
    "json":"true"
}

headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': "e9fedc27f1msh8cc22da28edb864p173db2jsn57c9343552b6"
    }

fmt = "%Y-%m-%dT%H:%M:%SZ"

class ListNasaTrivial(APIView):
    def get(self, request, *args, **kwargs):
        

        nasa_events = NasaEvent.objects.all().prefetch_related('solarEvent')
        for event in nasa_events:
            datestring = event.solarEvent.datetime
            dt = datetime.strptime(datestring, fmt)
            year = dt.year
            month = dt.month
            day = dt.day
            for i in range(5):              
                with transaction.atomic():
                    url = f"https://numbersapi.p.rapidapi.com/{month}/{day}/date"
                    response = requests.request("GET", url, headers=headers, params=querystring)

        result = response.json()
        return Response(response.json(), status.HTTP_200_OK)

