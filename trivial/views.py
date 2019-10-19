from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

url = "https://numbersapi.p.rapidapi.com/6/21/date"

querystring = {"fragment":"true","json":"true"}

headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': "e9fedc27f1msh8cc22da28edb864p173db2jsn57c9343552b6"
    }


class ListNasaTrivial(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response(dict(result=response), status.HTTP_200_OK)

