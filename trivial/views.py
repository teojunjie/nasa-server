from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from nasa.models import (
    NasaEvent
)
from .models import Trivial
from .serializers import TrivialSerializer
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

fmt = "%Y-%m-%d"

class ListNasaTrivial(APIView):
    def get(self, request, *args, **kwargs):
        
        trivial_data = []
        nasa_events = NasaEvent.objects.all().prefetch_related('solarEvent')
        for event in nasa_events:
            datestring = event.solarEvent.datetime
            date, _ = str(datestring).split(' ')
            dt = datetime.strptime(date, fmt)
            month = dt.month
            day = dt.day
        
            with transaction.atomic():
                url = f"https://numbersapi.p.rapidapi.com/{month}/{day}/date"
                response = requests.request("GET", url, headers=headers, params=querystring)

                result = response.json()
                year = result.get("year")
                if year > 2000:
                    trivial = Trivial.objects.create(
                        fact=result.get("text"),
                        date=datetime(year, month, day),
                        nasa_event=event
                    )
                    serialized = TrivialSerializer(trivial)
                    trivial_data.append(serialized.data)
                

        return Response(dict(result=trivial_data), status.HTTP_200_OK)

