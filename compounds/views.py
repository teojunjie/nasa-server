from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pubchempy as pcp
import json
from .models import Compound
from django.db import transaction
from .serializers import CompoundSerializer
from rest_framework.generics import ListAPIView
from .serializers import CompoundSerializer

class CreateCompoundView(APIView):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        melting_point = body.get('melting_point')
        boiling_point = body.get('boiling_point')
        compound_name = kwargs.get('compound_name')
        compound = pcp.get_compounds(compound_name, 'name')[0]
        compound_data = compound.to_dict(properties=['molecular_weight'])

        with transaction.atomic():
            compound = Compound.objects.create(
                melting_point=melting_point,
                boiling_point=boiling_point,
                molecular_weight=compound_data.get('molecular_weight'),
                name=compound_name,
            )
            serialized_compound = CompoundSerializer(compound)

        return Response(
            dict(result=serialized_compound.data),
            status=status.HTTP_200_OK,
        )


class ListCompoundsView(ListAPIView):
    queryset = Compound.objects.all()
    serializer_class = CompoundSerializer