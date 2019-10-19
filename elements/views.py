from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Element

ELEMENTS_API_URL = "https://neelpatel05.pythonanywhere.com/"

class PopulateElements(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.request("GET", ELEMENTS_API_URL)
        # for element in response.json():
        #     Element.objects.create(

        #     )

        return Response(
            dict(result=response.json()),
            status.HTTP_200_OK
        )
