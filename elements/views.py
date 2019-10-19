from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Element
from django.db import transaction
from rest_framework.generics import ListAPIView
from .serializers import ElementSerializer

ELEMENTS_API_URL = "https://neelpatel05.pythonanywhere.com/"

class PopulateElements(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.request("GET", ELEMENTS_API_URL)
        for element in response.json():
            print(element)
            with transaction.atomic():
                element = Element.objects.create(
                    atomic_mass=element.get('atomicMass'),
                    atomic_number=str(element.get('atomicNumber')),
                    atomic_radius=str(element.get('atomicRadius')),
                    boiling_point=str(element.get('bondingType')),
                    cpk_hex_color=element.get('cpkHexColor'),
                    density=str(element.get('density')),
                    electron_affinity=str(element.get('electronAffinity')),
                    electronegativity=str(element.get('electronegativity')),
                    electronic_configuration=element.get('electronicConfiguration'),
                    group_block=element.get('groupBlock'),
                    ion_radius=element.get('ionRadius'),
                    ionization_energy=element.get('ionizationEnergy'),
                    melting_point=str(element.get('meltingPoint')),
                    name=element.get('name'),
                    oxidation_states=element.get('oxidataionStates'),
                    standard_state=element.get('standardState'),
                    symbol=element.get('symbol'),
                    van_der_waal_radius=str(element.get('vanDelWaaalRadius')),
                    year_discovered=str(element.get('yearDiscovered')),
                )

        return Response(
            'Elements saved to database',
            status.HTTP_200_OK
        )


class ListPeriodicElements(ListAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class GetPeriodicElement(APIView):
    def get(self, request, *args, **kwargs):
        element_name = kwargs.get('element_name')

        element = Element.objects.filter(name=element_name)
        serialized_element = ElementSerializer(element)

        return Response(
            dict(result=serialized_element.data),
            status.HTTP_200_OK,
        )