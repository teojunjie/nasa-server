from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import os
import datetime
from nasa.models import (
    NasaEvent,
    SolarFlare,
    SolarBody,
)
from .serializers import (
    SolarFlareSerializer,
    NasaEventSerializer,
    SolarBodySerializer,
)
from django.core import serializers
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

NASA_API_KEY = os.environ['NASA_API_KEY']
SOLAR_FLARE_NASA_URL = "https://api.nasa.gov/DONKI/FLR"
SOLAR_FLARE_QUERY_STRING = {
    "startDate":"2015-01-01",
    "endDate":"2019-01-01",
    "api_key": NASA_API_KEY
}

MINIMUM_SOLAR_MAGNITUDE_EVENT = 5

fmt = "%Y-%m-%dT%H:%MZ"

class SaveSolarFlareView(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.request("GET", SOLAR_FLARE_NASA_URL, params=SOLAR_FLARE_QUERY_STRING)
        result = response.json()
        filtered_solared_events = []
        for event in result:
            classType = event.get('classType')
            stripped_solar_magnitude = float(classType[1:])
            if stripped_solar_magnitude > MINIMUM_SOLAR_MAGNITUDE_EVENT:
                filtered_solared_events.append(event)

        response_data = []
        for event in filtered_solared_events:
            dt = datetime.datetime.strptime(event.get('peakTime'), fmt)
            with transaction.atomic():                
                solarflare = SolarFlare.objects.create(
                    classType=event.get('classType'),
                    datetime=dt,
                    name=event.get('flrID'),
                )
                nasaEvent = NasaEvent.objects.create(
                    event='solar',
                    solarEvent=solarflare,
                )
                serialized_nasa_event_data = NasaEventSerializer(nasaEvent)
                serialized_solar_data = SolarFlareSerializer(solarflare)
                
                result = dict(
                    solar=serialized_solar_data.data,
                    event=serialized_nasa_event_data.data,
                )
                
                response_data.append(result)

        return Response(
            dict(
                result=response_data,
                count=len(filtered_solared_events)),
            status.HTTP_200_OK
        )

NASA_API_KEY = os.environ['NASA_API_KEY']
SOLAR_BODIES_URL = "https://api.le-systeme-solaire.net/rest/bodies?"
SOLAR_BODIES_QUERY_STRING = {
    "data": "id,englishName,isPlanet,dimension,gravity,meanRadius"
}

class SaveSolarBodyView(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.request("GET", SOLAR_BODIES_URL, params=SOLAR_BODIES_QUERY_STRING)
        res = response.json()

        bodies = res.get("bodies")

        serializedBodies = []
        for body in bodies:
            # create solar body obj
            solarBody = SolarBody.objects.create(
                englishName=body.get('englishName'),
                isPlanet=body.get('isPlanet'),
                dimension=body.get('dimension'),
                gravity=body.get('gravity'),
                meanRadius=body.get('meanRadius'),
            )

            serializedBody = SolarBodySerializer(solarBody)
            result = dict(solarBody = serializedBody.data)
            serializedBodies.append(result)

        return Response(
            dict(
                result=serializedBodies, 
                count=len(serializedBodies)),
            status.HTTP_200_OK
        )

class GetSolarBodyView(APIView):
    def get(self, request, *args, **kwargs):
        solarBodyName = kwargs.get('solarbody_name')

        try:
            solarBodies = SolarBody.objects.filter(englishName__icontains=solarBodyName)

            serializedBodies = []
            for solarBody in solarBodies:
                serializedBody = SolarBodySerializer(solarBody)
                result = dict(solarBody = serializedBody.data)
                serializedBodies.append(result)
            
            return Response(
                dict(
                    result=serializedBodies,
                    count=len(serializedBodies)
                ),
                status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                dict(
                    result=None,
                    count=0
                ),
                status=status.HTTP_200_OK) 
