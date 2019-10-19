from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ListNasaTrivial(APIView):
    def get(self, request, *args, **kwargs):
        json_data = {'hello': 'world'}
        return Response(json_data, status.HTTP_200_OK)

